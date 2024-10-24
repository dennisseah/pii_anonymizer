import pytest

from pii_anonymizer.services.presidio_text_analyzer import PresidioTextAnalyzer


@pytest.mark.asyncio
async def test_presidio_text_analyzer():
    analyzer = PresidioTextAnalyzer()
    text = "John Doe"

    analyzed = await analyzer.analyze(text, ["PERSON"])
    assert len(analyzed) == 1
    assert analyzed[0].type == "PERSON"


@pytest.mark.asyncio
async def test_presidio_text_analyzer_no_type():
    analyzer = PresidioTextAnalyzer()
    text = "John Doe"

    analyzed = await analyzer.analyze(text, [])
    assert len(analyzed) == 0
