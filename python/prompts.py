import requests
from smolagents import CODE_SYSTEM_PROMPT
from config import settings

DOCUMENT_CONTEXT_PROMPT = """
<document>
{doc_content}
</document>
"""

CHUNK_CONTEXT_PROMPT = """
Here is the chunk we want to situate within the whole document
<chunk>
{chunk_content}
</chunk>

Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.
Answer only with the succinct context and nothing else.
"""

QUERY_PROMPT = "Represent this sentence for searching relevant passages: "

SYSTEM_PROMPT_RULES = """
**Rules:**
- Use the VideoEditorTool with render=False first and wait for VisualFeedbackTool
- Depending on VisualFeedbackTool, use the VideoEditorTool with render=True to render the video
"""

def get_system_prompt():
    result = requests.get(f"{settings.url}/system-prompt.txt")

    return f"{CODE_SYSTEM_PROMPT}\n\n{result.text}\n\n{SYSTEM_PROMPT_RULES}"
