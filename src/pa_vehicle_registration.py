import asyncio
import os

from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()
sensitive_data = {
    "CURRENT_ODOMETER_READING": os.environ["CURRENT_ODOMETER_READING"],
    "TITLE_NUMBER_FIRST_EIGHT": os.environ["TITLE_NUMBER_FIRST_EIGHT"],
    "PLATE_NUMBER": os.environ["PLATE_NUMBER"],
    "INSURANCE_COMPANY_NAME": os.environ["INSURANCE_COMPANY_NAME"],
    "INSURANCE_POLICY_NUMBER": os.environ["INSURANCE_POLICY_NUMBER"],
    "INSURANCE_EFFECTIVE_DATE": os.environ["INSURANCE_EFFECTIVE_DATE"],
    "INSURANCE_EXPIRATION_DATE": os.environ["INSURANCE_EXPIRATION_DATE"],
    "INSURANCE_NAIC_NUMBER": os.environ["INSURANCE_NAIC_NUMBER"],
    "EMAIL_ADDRESS": os.environ["EMAIL_ADDRESS"],
}

task = """\
Navigate to https://www.pa.gov/services/dmv/renew-vehicle-registration.html to renew vehicle registration online.
Login using the TITLE_NUMBER and PLATE_NUMBER.
Proceed to renew the vehicle registration for 1 year.

Fill out the the form using the following variables:
- CURRENT_ODOMETER_READING
- TITLE_NUMBER_FIRST_EIGHT
- PLATE_NUMBER
- INSURANCE_COMPANY_NAME
- INSURANCE_POLICY_NUMBER
- INSURANCE_EFFECTIVE_DATE
- INSURANCE_EXPIRATION_DATE
- INSURANCE_NAIC_NUMBER
- EMAIL_ADDRESS

Stop when you get to the payment page."""


async def main():
    agent = Agent(
        task="Go to lasa.org and login to the online payment portal using LASA_USERNAME and LASA_PASSWORD. Then proceed to make a payment using the existing payment method.",
        llm=ChatOpenAI(model="gpt-4o"),
        sensitive_data=sensitive_data,
    )
    await agent.run()


asyncio.run(main())
