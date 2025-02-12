from langchain_openai import ChatOpenAI
from browser_use import Agent, BrowserConfig, Browser
from pydantic import SecretStr
from dotenv import load_dotenv
import asyncio
import argparse
import os
import subprocess

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY", "")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")


browser = Browser(
    config=BrowserConfig(
        chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS path
    )
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=SecretStr(api_key),
)


async def RunAgent(agent: Agent):
    result = await agent.run()
    print(result.final_result())


def GetArgs():
    parser = argparse.ArgumentParser(description="Run agent with custom task")
    parser.add_argument(
        "--task",
        type=str,
        default="Search what is the tallest ferris wheel in the world and write to a google doc",
        help="Specify the task for the agent",
    )
    args = parser.parse_args()
    return args


def CreateAgent(args):
    agent = Agent(
        task=args.task,
        llm=llm,
        use_vision=False,
        max_failures=5,
        browser=browser,
    )
    return agent


def main():
    # forcefully closes any existing chrome tabs
    subprocess.call("pkill -9 -f 'Google Chrome'", shell=True)

    args = GetArgs()
    agent = CreateAgent(args)
    asyncio.run(RunAgent(agent))


if __name__ == "__main__":
    main()
