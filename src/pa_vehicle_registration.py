import asyncio
import os
import time

from pathlib import Path
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserContextConfig
from browser_use.browser.context import BrowserContext

from dotenv import load_dotenv

load_dotenv(".env.pvr")
sensitive_data = {
    "TITLE_NUMBER_FIRST_EIGHT": os.environ["TITLE_NUMBER_FIRST_EIGHT"],
    "PLATE_NUMBER": os.environ["PLATE_NUMBER"],
    "CURRENT_ODOMETER_READING": os.environ["CURRENT_ODOMETER_READING"],
    "INSURANCE_COMPANY_NAME": os.environ["INSURANCE_COMPANY_NAME"],
    "INSURANCE_POLICY_NUMBER": os.environ["INSURANCE_POLICY_NUMBER"],
    "INSURANCE_EFFECTIVE_DATE_YYYY": os.environ["INSURANCE_EFFECTIVE_DATE_YYYY"],
    "INSURANCE_EFFECTIVE_DATE_MM": os.environ["INSURANCE_EFFECTIVE_DATE_MM"],
    "INSURANCE_EFFECTIVE_DATE_DD": os.environ["INSURANCE_EFFECTIVE_DATE_DD"],
    "INSURANCE_EXPIRATION_DATE_YYYY": os.environ["INSURANCE_EXPIRATION_DATE_YYYY"],
    "INSURANCE_EXPIRATION_DATE_MM": os.environ["INSURANCE_EXPIRATION_DATE_MM"],
    "INSURANCE_EXPIRATION_DATE_DD": os.environ["INSURANCE_EXPIRATION_DATE_DD"],
    "INSURANCE_NAIC_NUMBER": os.environ["INSURANCE_NAIC_NUMBER"],
    "EMAIL_ADDRESS": os.environ["EMAIL_ADDRESS"],
}

task = """\
Navigate to https://www.pa.gov/services/dmv/renew-vehicle-registration.html to renew vehicle registration online.
Login using the TITLE_NUMBER_FIRST_EIGHT and PLATE_NUMBER.
Proceed to renew the vehicle registration for 1 year.

Fill out the the form using the following variables:
- CURRENT_ODOMETER_READING
- INSURANCE_COMPANY_NAME
- INSURANCE_POLICY_NUMBER
- INSURANCE_NAIC_NUMBER
- INSURANCE_EFFECTIVE_DATE_YYYY
- INSURANCE_EFFECTIVE_DATE_MM
- INSURANCE_EFFECTIVE_DATE_DD
- INSURANCE_EXPIRATION_DATE_YYYY
- INSURANCE_EXPIRATION_DATE_MM
- INSURANCE_EXPIRATION_DATE_DD

NOTE: clear any existing values before filling in new values.

Check the box with the disclaimer that the registration will only be sent digitally.
We want to send the registration to EMAIL_ADDRESS, which we will input on a later page.

Stop when you successfully submit this information."""

run_id = f"{int(time.time())}"
runs_dir = Path(__file__).parent.parent.joinpath("runs")
run_dir = runs_dir.joinpath(f"run_{run_id}")
run_dir.mkdir(parents=True)
print(f"Created run directory: {run_dir}")
conversation_path = run_dir.joinpath("conversation")

browser = Browser()
browser_context_config = BrowserContextConfig(save_recording_path=str(run_dir))
browser_context = BrowserContext(browser, browser_context_config)


async def main():
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o"),
        sensitive_data=sensitive_data,
        save_conversation_path=str(conversation_path),
        browser_context=browser_context,
    )
    await agent.run()


asyncio.run(main())
