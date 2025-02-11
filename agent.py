from langchain_openai import ChatOpenAI
from browser_use import Agent, BrowserConfig
from pydantic import SecretStr
from dotenv import load_dotenv
import asyncio
import argparse
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY', '')
if not api_key:
	raise ValueError('OPENAI_API_KEY is not set')



# Initialize the model
llm=ChatOpenAI(
    model='gpt-4o-mini',
    api_key=SecretStr(api_key),
)

async def RunAgent(agent: Agent):
    result = await agent.run()
    print(result.final_result())


def main():

    parser = argparse.ArgumentParser(description="Run agent with custom task")
    parser.add_argument("--task", type=str, default="Search what is the tallest ferris wheel in the world", help="Specify the task for the agent")
    args = parser.parse_args()

    agent = Agent(
    task=args.task,
    llm=llm,
    use_vision=False,
    max_failures=5,
    )

    asyncio.run(RunAgent(agent))

if __name__ == "__main__":
    main()