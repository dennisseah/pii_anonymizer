import asyncio

from faker import Faker

from pii_anonymizer.generators.datetime_generator import DateTimeGenerator
from pii_anonymizer.generators.email_generator import EmailGenerator
from pii_anonymizer.generators.ip_address_generator import IPAddressGenerator
from pii_anonymizer.generators.label_generator import LabelGenerator
from pii_anonymizer.generators.mask_generator import MaskGenerator
from pii_anonymizer.generators.name_generator import NameGenerator
from pii_anonymizer.hosting import container
from pii_anonymizer.protocols.i_text_analyzer import ITextAnalyzer
from pii_anonymizer.protocols.i_text_anonymizer import ITextAnonymizer

# sample code to show how to use the text analyzer and text anonymizer
# there are 3 entities in the text: PERSON, PHONE_NUMBER, CREDIT_CARD

text = """Her name is Mary Ann. My name is James Bond. My phone number is 212-555-5555.
My credit card is 5548364515335857. Again my name is James Bond and number is
212-555-5555. My email address is jbond@secret-service.com. My IP address is
120.10.0.1. The time is 2022-10-01X13:00:00."""

print("Original text:")
print(text)
print()

# seed the faker so that the generated data is consistent
Faker.seed(100)

# set the mask character for the CREDIT_CARD entity default is "*" for masking
MaskGenerator.mask_char_mapping["CREDIT_CARD"] = "X"

# set the date range for the DATE_TIME entity default is 10
# plus/minus 20 days from the original date
DateTimeGenerator.date_range = 20


async def main():
    # get the text analyzer from the DI container
    text_analyzer = container[ITextAnalyzer]

    analyzed_result = await text_analyzer.analyze(
        text=text,
        entities=[
            "PERSON",
            "PHONE_NUMBER",
            "CREDIT_CARD",
            "EMAIL_ADDRESS",
            "DATE_TIME",
            "IP_ADDRESS",
        ],
        language="en",
    )

    print("Analyzed result:")
    print(analyzed_result)
    print()

    # get the text anonymizer from the DI container
    text_anonymizer = container[ITextAnonymizer]

    anonymized_result = await text_anonymizer.anonymize(
        text=text,
        analyzer_results=analyzed_result,
        operators={
            "PERSON": NameGenerator,
            "PHONE_NUMBER": LabelGenerator,
            "CREDIT_CARD": MaskGenerator,
            "EMAIL_ADDRESS": EmailGenerator,
            "DATE_TIME": DateTimeGenerator,
            "IP_ADDRESS": IPAddressGenerator,
        },
    )

    print("Anonymized result:")
    print(anonymized_result)
    print()

    print("Anonymized text:")
    print(anonymized_result.text)
    print()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
