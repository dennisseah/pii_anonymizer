from typing import Protocol

from pii_anonymizer.models.text_analyzed_result import (
    TextAnalyzedResult,
    TextAnalyzerType,
)


class ITextAnalyzer(Protocol):
    """Protocol for Text Analyzer Service."""

    async def analyze(
        self, text: str, entities: list[TextAnalyzerType], language: str = "en"
    ) -> list[TextAnalyzedResult]: ...
