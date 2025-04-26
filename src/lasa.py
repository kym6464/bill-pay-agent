import asyncio
import os

from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()
sensitive_data = {
    "LASA_USERNAME": os.environ["LASA_USERNAME"],
    "LASA_PASSWORD": os.environ["LASA_PASSWORD"],
}


async def main():
    agent = Agent(
        task="Go to lasa.org and login to the online payment portal using LASA_USERNAME and LASA_PASSWORD. Then proceed to make a payment using the existing payment method.",
        llm=ChatOpenAI(model="gpt-4o"),
        sensitive_data=sensitive_data,
    )
    await agent.run()


asyncio.run(main())
