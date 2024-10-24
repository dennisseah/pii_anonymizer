from pii_anonymizer.models.text_analyzed_result import TextAnalyzedResult


def test_text_analyzed_result():
    text_analyzed_result = TextAnalyzedResult(
        start=0,
        end=10,
        score=0.5,
        type="PERSON",
    )
    assert text_analyzed_result.start == 0
    assert text_analyzed_result.end == 10
    assert text_analyzed_result.score == 0.5
    assert text_analyzed_result.type == "PERSON"
