import asyncio
from agent import Agent


async def main():
    agent = Agent(
        assets=["assets/big_buck_bunny_1080p_30fps.mp4"],
        task="Add a 150 second subclip to the video",
        llm=None,
    )
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
