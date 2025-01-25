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
    print(result)


def main():

    parser = argparse.ArgumentParser(description="Run agent with custom task")
    parser.add_argument("--task", type=str, default="Compare O4 to DeepSeek, and save as a PDF. Only use a text editor online that does not require signing in", help="Specify the task for the agent")
    args = parser.parse_args()

    agent = Agent(
    task=args.task,
    llm=llm,
    use_vision=False,
    )

    asyncio.run(RunAgent(agent))

if __name__ == "__main__":
    main()