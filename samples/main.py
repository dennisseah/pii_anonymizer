import asyncio

from faker import Faker

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
212-555-5555."""
print("Original text:")
print(text)
print()

# seed the faker so that the generated data is consistent
Faker.seed(100)

# set the mask character for the CREDIT_CARD entity default is "*" for masking
MaskGenerator.mask_char_mapping["CREDIT_CARD"] = "X"


async def main():
    # get the text analyzer from the DI container
    text_analyzer = container[ITextAnalyzer]

    analyzed_result = await text_analyzer.analyze(
        text=text,
        entities=["PERSON", "PHONE_NUMBER", "CREDIT_CARD"],
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
            "PERSON": NameGenerator(),
            "PHONE_NUMBER": LabelGenerator(),
            "CREDIT_CARD": MaskGenerator(),
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
