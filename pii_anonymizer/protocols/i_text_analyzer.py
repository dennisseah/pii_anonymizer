from typing import Protocol

from pii_anonymizer.models.text_analyzed_result import (
    TextAnalyzedResult,
    TextAnalyzerType,
)


class ITextAnalyzer(Protocol):
    """Protocol for Text Analyzer Service."""

    async def analyze(
        self, text: str, entities: list[TextAnalyzerType], language: str = "en"
    ) -> list[TextAnalyzedResult]:
        """
        Analyze the text for the given entities.

        :param text : The text to analyze.
        :param entities : The entities to analyze.
        :param language : The language of the text. Default is "en".
        :return : The analyzed result.
        """
        ...
