from dataclasses import dataclass

from presidio_analyzer import AnalyzerEngine

from pii_anonymizer.models.text_analyzed_result import (
    TextAnalyzedResult,
    TextAnalyzerType,
)
from pii_anonymizer.protocols.i_text_analyzer import ITextAnalyzer


@dataclass
class PresidioTextAnalyzer(ITextAnalyzer):
    """Text Analyzer Service using Presidio."""

    async def analyze(
        self, text: str, entities: list[TextAnalyzerType], language: str = "en"
    ) -> list[TextAnalyzedResult]:
        """Analyze the text and return the results."""

        if len(entities) == 0:
            return []

        analyzer = AnalyzerEngine()
        entities_type = [str(e) for e in entities]
        results = analyzer.analyze(text=text, entities=entities_type, language=language)

        return [
            TextAnalyzedResult(
                type=result.entity_type,
                start=result.start,
                end=result.end,
                score=result.score,
            )
            for result in results
            if result.entity_type in entities
        ]
