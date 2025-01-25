from langchain_openai import ChatOpenAI
from browser_use import Agent, BrowserConfig
from pydantic import SecretStr
from dotenv import load_dotenv
load_dotenv()
import asyncio
import argparse

# Initialize the model
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat')


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
    )

    asyncio.run(RunAgent(agent))

if __name__ == "__main__":
    main()