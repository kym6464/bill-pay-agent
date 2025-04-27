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
    "INSURANCE_NAIC_NUMBER": os.environ["INSURANCE_NAIC_NUMBER"],
    "INSURANCE_EFFECTIVE_DATE_YYYY": os.environ["INSURANCE_EFFECTIVE_DATE_YYYY"],
    "INSURANCE_EFFECTIVE_DATE_MM": os.environ["INSURANCE_EFFECTIVE_DATE_MM"],
    "INSURANCE_EFFECTIVE_DATE_DD": os.environ["INSURANCE_EFFECTIVE_DATE_DD"],
    "INSURANCE_EXPIRATION_DATE_YYYY": os.environ["INSURANCE_EXPIRATION_DATE_YYYY"],
    "INSURANCE_EXPIRATION_DATE_MM": os.environ["INSURANCE_EXPIRATION_DATE_MM"],
    "INSURANCE_EXPIRATION_DATE_DD": os.environ["INSURANCE_EXPIRATION_DATE_DD"],
    "EMAIL_ADDRESS": os.environ["EMAIL_ADDRESS"],
    "CREDIT_CARD_NUMBER": os.environ["CREDIT_CARD_NUMBER"],
    "CREDIT_CARD_EXPIRATION_MM": os.environ["CREDIT_CARD_EXPIRATION_MM"],
    "CREDIT_CARD_EXPIRATION_YY": os.environ["CREDIT_CARD_EXPIRATION_YY"],
    "CREDIT_CARD_EXPIRATION_YYYY": os.environ["CREDIT_CARD_EXPIRATION_YYYY"],
    "CREDIT_CARD_SECURITY_CODE": os.environ["CREDIT_CARD_SECURITY_CODE"],
    "CREDIT_CARD_CARDHOLDER_NAME": os.environ["CREDIT_CARD_CARDHOLDER_NAME"],
    "CREDIT_CARD_ADDRESS_STREET": os.environ["CREDIT_CARD_ADDRESS_STREET"],
    "CREDIT_CARD_ADDRESS_CITY": os.environ["CREDIT_CARD_ADDRESS_CITY"],
    "CREDIT_CARD_ADDRESS_STATE": os.environ["CREDIT_CARD_ADDRESS_STATE"],
    "CREDIT_CARD_ADDRESS_ZIP": os.environ["CREDIT_CARD_ADDRESS_ZIP"],
}

task = f"""\
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

Decline any requests for donations and continue.

On the Shopping Cart page, where you are asked to enter the EMAIL_ADDRESS, you
first need to select "I would like to check out" and check the confirmation
box before you are able to enter the email address.

Fill out the information on the payment page.
The credit card state is {os.environ["CREDIT_CARD_ADDRESS_STATE"]}."""

run_id = f"{int(time.time())}"
runs_dir = Path(__file__).parent.parent.joinpath("runs")
run_dir = runs_dir.joinpath(f"run_{run_id}")
run_dir.mkdir(parents=True)
print(f"Created run directory: {run_dir}")
conversation_path = run_dir.joinpath("conversation")

browser = Browser()
browser_context_config = BrowserContextConfig(
    save_recording_path=str(run_dir),
    keep_alive=True,
    wait_for_network_idle_page_load_time=3,
)
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
    input("Done! Press any key to exit...")


asyncio.run(main())
