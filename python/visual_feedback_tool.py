import os
import tempfile
import base64
import time
import anthropic
import asyncio
import instructor
from pydantic import BaseModel, Field
from enum import Enum
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.text import Text

from smolagents import Tool
from diffusion_studio import DiffusionClient
from typing import Dict, Any, List
from loguru import logger
from core_tool import VideoEditorTool


class Severity(str, Enum):
    CRITICAL = "critical"
    WARNING = "warning"
    INFO = "info"


class CompositionIssue(BaseModel):
    description: str
    severity: Severity
    category: str = Field(
        ..., description="Category of the issue: composition, technical, or transition"
    )


class FrameAnalysis(BaseModel):
    composition_quality: str = Field(
        ..., description="Analysis of framing, balance, and visual flow"
    )
    technical_issues: str = Field(
        ..., description="Analysis of artifacts, glitches, and quality loss"
    )
    transition_potential: str = Field(
        ..., description="Analysis of how well the frame would cut/transition"
    )
    issues: List[CompositionIssue] = Field(
        default_factory=list, description="List of detected issues"
    )


class RenderDecision(BaseModel):
    status: str = Field(
        ..., description="Status of the render decision: 'blocked', 'warning', 'ready'"
    )
    score: float = Field(..., description="Overall quality score")
    technical_score: float = Field(..., description="Technical quality score")
    composition_score: float = Field(..., description="Composition quality score")
    critical_issues: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    suggestions: List[str] = Field(default_factory=list)
    frame_analysis: Dict[str, FrameAnalysis] = Field(...)
    stats: Dict[str, Any] = Field(...)


class VisualFeedbackTool(Tool):
    name = "visual_feedback"
    description = """Analyzes video composition quality and makes render decisions.
    Works in conjunction with VideoEditorTool to validate edits before rendering.
    Uses frame sampling and Vision Language Model to assess:
    - Technical quality (artifacts, glitches)
    - Composition quality (framing, balance)
    - Transition potential

    Returns a RenderDecision with status:
    - 'ready': High quality, proceed with render
    - 'warning': Issues that should be addressed
    - 'blocked': Critical issues preventing render"""

    inputs = {
        "final_goal": {
            "type": "string",
            "description": "Quality criteria to evaluate (e.g. 'Ensure smooth transitions', 'Check for visual artifacts')",
            "nullable": False,
            "required": True,
        },
    }
    output_type = "object"  # Returns RenderDecision

    def __init__(self, client: DiffusionClient):
        super().__init__()
        # Use async client directly with instructor
        base_client = anthropic.AsyncAnthropic()
        self.anthropic_client = instructor.from_anthropic(base_client)
        self.model = "claude-3-5-sonnet-latest"
        self.client = client
        self.temp_dir = tempfile.mkdtemp()

    async def _analyze_image_async(self, image_path: str, prompt: str) -> FrameAnalysis:
        """Analyze image using Claude Vision asynchronously"""
        try:
            with open(image_path, "rb") as f:
                image_data = base64.b64encode(f.read()).decode()

            media_type = "image/jpeg" if image_path.endswith(".jpg") else "image/png"

            # Use async client directly
            analysis = await self.anthropic_client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {  # type: ignore
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": media_type,
                                    "data": image_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": prompt,
                            },
                        ],
                    }
                ],
                response_model=FrameAnalysis,
            )
            return analysis

        except Exception as e:
            logger.error(f"Error analyzing image {image_path}: {str(e)}")
            return FrameAnalysis(
                composition_quality="Error analyzing frame",
                technical_issues="Error analyzing frame",
                transition_potential="Error analyzing frame",
                issues=[
                    CompositionIssue(
                        description=str(e),
                        severity=Severity.CRITICAL,
                        category="technical",
                    )
                ],
            )

    async def _process_frames(
        self, frame_paths: List[str], final_goal: str
    ) -> Dict[str, Dict[str, Any]]:
        """Process all frames with progress tracking"""
        prompt = f"""Analyze this frame for editing goal: '{final_goal}'
        Focus ONLY on editing and composition quality, not scene content.
        Provide a structured analysis with these components:

        1. Composition quality: Evaluate framing, balance, and visual flow (10-15 words)
        2. Technical issues: Note any artifacts, glitches, or quality loss (10-15 words)
        3. Transition potential: Assess how well it would cut/transition (10-15 words)

        For each component, if you spot issues, classify them by severity:
        - CRITICAL: Major glitches, artifacts, or errors that must be fixed
        - WARNING: Quality issues that should be addressed
        - INFO: Minor suggestions for improvement
        """

        try:
            analyses = await asyncio.gather(
                *[
                    self._analyze_image_async(os.path.join("samples", frame), prompt)
                    for frame in frame_paths
                ]
            )

            results = {}
            for i, (frame_name, analysis) in enumerate(zip(frame_paths, analyses), 1):
                frame_path = os.path.join("samples", frame_name)
                results[f"frame_{i}"] = {"frame_path": frame_path, "analysis": analysis}

                try:
                    os.remove(frame_path)
                    logger.debug(f"Deleted frame: {frame_path}")
                except Exception as e:
                    logger.warning(f"Failed to delete frame {frame_path}: {e}")

            return results

        except Exception as e:
            logger.error(f"Error processing frames: {str(e)}")
            return {
                "error": {
                    "frame_path": "",
                    "analysis": FrameAnalysis(
                        composition_quality="Error processing frames",
                        technical_issues=str(e),
                        transition_potential="Error processing frames",
                        issues=[
                            CompositionIssue(
                                description=str(e),
                                severity=Severity.CRITICAL,
                                category="technical",
                            )
                        ],
                    ),
                }
            }

    def _make_decision(self, results: Dict[str, Dict[str, Any]]) -> RenderDecision:
        """Process analysis results and make render decision"""
        critical_issues = []
        warnings = []
        suggestions = []
        frame_count = 0
        good_frames = []
        frame_analyses = {}

        for timestamp, data in results.items():
            frame_count += 1
            analysis: FrameAnalysis = data["analysis"]
            frame_analyses[timestamp] = analysis

            if not any(
                issue.severity == Severity.CRITICAL for issue in analysis.issues
            ):
                good_frames.append(timestamp)

            for issue in analysis.issues:
                if issue.severity == Severity.CRITICAL:
                    critical_issues.append(
                        f"{timestamp}: {issue.description} ({issue.category})"
                    )
                elif issue.severity == Severity.WARNING:
                    warnings.append(
                        f"{timestamp}: {issue.description} ({issue.category})"
                    )
                else:
                    suggestions.append(
                        f"{timestamp}: {issue.description} ({issue.category})"
                    )

        # Calculate quality metrics
        technical_score = (frame_count - len(critical_issues)) / frame_count * 100
        composition_score = (frame_count - len(warnings)) / frame_count * 100
        overall_score = (
            technical_score * 0.6 + composition_score * 0.4
        )  # Weight technical issues more

        # Compile stats
        stats = {
            "total_frames": frame_count,
            "good_frames": len(good_frames),
            "good_frames_percentage": (len(good_frames) / frame_count * 100)
            if frame_count > 0
            else 0,
            "critical_issues_count": len(critical_issues),
            "warnings_count": len(warnings),
            "suggestions_count": len(suggestions),
        }

        # Determine status
        if critical_issues:
            status = "blocked"
        elif overall_score < 80:
            status = "warning"
        else:
            status = "ready"

        return RenderDecision(
            status=status,
            score=overall_score,
            technical_score=technical_score,
            composition_score=composition_score,
            critical_issues=critical_issues[:5],  # Top 5 critical issues
            warnings=warnings[:5],  # Top 5 warnings
            suggestions=suggestions[:3],  # Top 3 suggestions
            frame_analysis=frame_analyses,
            stats=stats,
        )

    def forward(
        self,
        final_goal: str = "The video should show a smooth transition between scenes without any glitches or artifacts.",
    ) -> Any:
        """Process video frames and get feedback."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            # If no loop is running, create a new one
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                return loop.run_until_complete(self._async_forward(final_goal))
            finally:
                loop.close()
        else:
            # If we're already in an event loop, just create the coroutine
            return loop.create_task(self._async_forward(final_goal))

    async def _async_forward(
        self,
        final_goal: str,
    ) -> RenderDecision:
        """Async implementation of the forward method."""
        try:
            await self.client.evaluate("""await sample()""")
            logger.info("Generated sample frame")

            frames = sorted(
                [f for f in os.listdir("samples") if f.startswith("sample-")]
            )
            logger.info(f"Found {len(frames)} frames to analyze")

            results = await self._process_frames(frames, final_goal)
            return self._make_decision(results)

        except Exception as e:
            logger.error("Video analysis failed")
            raise e

    def __del__(self):
        """Cleanup temp files"""
        import shutil

        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def display_analysis(self, decision: RenderDecision) -> None:
        console = Console()

        """Display analysis results in a pretty format"""
        # Create frame analysis table
        frame_table = Table(
            title="🎬 Frame Analysis",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta",
        )
        frame_table.add_column("Frame", style="cyan")
        frame_table.add_column("Composition", style="green")
        frame_table.add_column("Technical", style="blue")
        frame_table.add_column("Transitions", style="yellow")

        for timestamp, analysis in decision.frame_analysis.items():
            if analysis.issues:  # Only show frames with issues
                frame_table.add_row(
                    timestamp,
                    Text(analysis.composition_quality, style="green"),
                    Text(analysis.technical_issues, style="blue"),
                    Text(analysis.transition_potential, style="yellow"),
                )

        # Print analysis summary
        console.print("\n")
        console.print(frame_table)

        # Create stats panel
        stats_table = Table.grid(padding=1)
        stats_table.add_column(style="cyan", justify="right")
        stats_table.add_column(style="green")
        stats_table.add_row("Total Frames:", str(decision.stats["total_frames"]))
        stats_table.add_row(
            "Frames Without Issues:",
            f"{decision.stats['good_frames']} ({decision.stats['good_frames_percentage']:.1f}%)",
        )
        stats_table.add_row(
            "Critical Issues:", str(decision.stats["critical_issues_count"])
        )
        stats_table.add_row("Warnings:", str(decision.stats["warnings_count"]))
        stats_table.add_row("Suggestions:", str(decision.stats["suggestions_count"]))

        console.print(
            Panel(
                stats_table,
                title="📊 Analysis Summary",
                border_style="blue",
                padding=(1, 2),
            )
        )

        # Create quality score panel
        quality_table = Table.grid(padding=1)
        quality_table.add_column(style="cyan", justify="right")
        quality_table.add_column(style="green")
        quality_table.add_row("Technical Score:", f"{decision.technical_score:.1f}%")
        quality_table.add_row(
            "Composition Score:", f"{decision.composition_score:.1f}%"
        )
        quality_table.add_row("Overall Quality:", f"{decision.score:.1f}%")

        console.print(
            Panel(
                quality_table,
                title="🎯 Quality Metrics",
                border_style="green",
                padding=(1, 2),
            )
        )

        # Handle decision
        if decision.status == "blocked":
            logger.error("⛔ Critical issues detected - Render blocked")
            console.print(
                Panel(
                    "\n".join(
                        [
                            "[red]⛔ Critical Issues Detected[/red]",
                            "",
                            "[yellow]High Priority Items:[/yellow]",
                            *[f"• {issue}" for issue in decision.critical_issues],
                            "",
                            "[cyan]Next Steps:[/cyan]",
                            "1. Review and fix critical issues",
                            "2. Focus on technical problems first",
                            "3. Run analysis again",
                        ]
                    ),
                    title="🚫 Render Blocked",
                    border_style="red",
                    padding=(1, 2),
                )
            )
            return

        if decision.status == "warning":
            logger.warning("⚠️ Quality improvements recommended")
            console.print(
                Panel(
                    "\n".join(
                        [
                            "[yellow]⚠️ Quality Improvements Recommended[/yellow]",
                            "",
                            "Top Issues to Address:",
                            *[f"• {warning}" for warning in decision.warnings],
                            "",
                            "[cyan]Options:[/cyan]",
                            "• Review and address warnings",
                            "• Proceed with render if quality is acceptable",
                            "• Run analysis again after fixes",
                        ]
                    ),
                    title="⚠️ Quality Check",
                    border_style="yellow",
                    padding=(1, 2),
                )
            )
            return

        logger.info("✨ High quality composition - Ready to render")
        console.print(
            Panel(
                "\n".join(
                    [
                        "[green]✨ High Quality Composition[/green]",
                        "",
                        f"[cyan]Overall Quality Score: {decision.score:.1f}%[/cyan]",
                        "",
                        "Optional Enhancements Available:",
                        *[f"• {suggestion}" for suggestion in decision.suggestions],
                        "",
                        "[green]Ready to proceed with render![/green]",
                    ]
                ),
                title="🌟 Ready to Render",
                border_style="green",
                padding=(1, 2),
            )
        )


async def main():
    client = DiffusionClient()
    await client.init()

    try:
        core_tool = VideoEditorTool(client=client)
        tool = VisualFeedbackTool(client=client)

        # Step 1: Composition
        logger.info("🎬 Composing video...")
        await core_tool.forward(
            assets=["assets/big_buck_bunny_1080p_30fps.mp4"],
            js_code="""
            // Create a 150 frames subclip
            const videoFile = assets()[0];
            const video = new core.VideoClip(videoFile).subclip(0, 150);
            await composition.add(video);
            """,
            ready_to_render=False,  # Initial composition, will auto-append sample()
        )

        # Step 2: Analysis
        logger.info("🔍 Analyzing composition...")
        decision = await tool.forward(
            final_goal="""Analyze the video composition focusing on:
            1. Overall flow and pacing between scenes
            2. Visual consistency and quality
            3. Transition opportunities and potential issues

            Minor imperfections are acceptable if they don't impact the viewing experience.
            Focus on issues that would be noticeable to the average viewer."""
        )

        # Display analysis results
        tool.display_analysis(decision)

        if decision.status == "ready":
            logger.info("✨ Final video rendered successfully!")

            # Only proceed with render if status is ready
            output_path = f"output/render_{int(time.time())}.mp4"
            # Set output path in client before rendering
            client.output = output_path

            # Pass the decision status as ready_to_render flag
            await core_tool.forward(
                assets=["assets/big_buck_bunny_1080p_30fps.mp4"],
                js_code="""
                // Create a 150 frames subclip
                const videoFile = assets()[0];
                const video = new core.VideoClip(videoFile).subclip(0, 150);
                await composition.add(video);
                """,
                output=output_path,
                ready_to_render=decision.status
                == "ready",  # Will auto-append render() if ready
            )

        else:
            logger.warning("⚠️ Render skipped due to quality issues")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
