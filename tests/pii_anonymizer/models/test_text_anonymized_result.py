from pii_anonymizer.models.text_anonymized_result import (
    TextAnonymizedResult,
    TextAnonymizedResultItem,
)


def test_text_anonymized_result():
    item = TextAnonymizedResultItem(
        start=0,
        end=8,
        entity_type="PERSON",
        text="John Doe",
        operator="NameGenerator",
    )
    text_anonymized_result = TextAnonymizedResult(
        text="John Doe",
        items=[item],
    )
    assert text_anonymized_result.text == "John Doe"
    assert 1 == len(text_anonymized_result.items)
