import pytest

from pii_anonymizer.generators.label_generator import LabelGenerator
from pii_anonymizer.generators.name_generator import NameGenerator
from pii_anonymizer.generators.phone_generator import PhoneGenerator
from pii_anonymizer.services.presidio_text_analyzer import PresidioTextAnalyzer
from pii_anonymizer.services.presidio_text_anonymizer import PresidioTextAnonymizer


@pytest.mark.asyncio
async def test_presidio_text_anonymizer():
    text = "I am John Doe and my phone number is 555-555-5555."

    text_analyzer = PresidioTextAnalyzer()
    analyzed_result = await text_analyzer.analyze(
        text=text,
        entities=["PERSON", "PHONE_NUMBER"],
        language="en",
    )

    text_anonymizer = PresidioTextAnonymizer()
    anonymized_result = await text_anonymizer.anonymize(
        text=text,
        analyzer_results=analyzed_result,
        operators={
            "PERSON": LabelGenerator,
            "PHONE_NUMBER": LabelGenerator,
        },
    )

    assert (
        anonymized_result.text
        == "I am <person_1> and my phone number is <phone_number_1>."
    )


@pytest.mark.asyncio
async def test_presidio_text_anonymizer_no_entities():
    text = "I am John Doe and my phone number is 555-555-5555."

    text_anonymizer = PresidioTextAnonymizer()
    anonymized_result = await text_anonymizer.anonymize(
        text=text,
        analyzer_results=[],
        operators={
            "PERSON": NameGenerator,
            "PHONE_NUMBER": PhoneGenerator,
        },
    )

    assert anonymized_result.text == text
