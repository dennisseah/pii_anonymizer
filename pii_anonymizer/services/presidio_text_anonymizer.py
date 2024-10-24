from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig, RecognizerResult
from presidio_anonymizer.operators import Operator

from pii_anonymizer.models.text_analyzed_result import (
    TextAnalyzedResult,
    TextAnalyzerType,
)
from pii_anonymizer.models.text_anonymized_result import (
    TextAnonymizedResult,
    TextAnonymizedResultItem,
)
from pii_anonymizer.protocols.i_text_anonymizer import ITextAnonymizer


class PresidioTextAnonymizer(ITextAnonymizer):
    """Protocol for Text Anonymizer Service."""

    def format_recognizer_results(
        self, analyzer_results: list[TextAnalyzedResult]
    ) -> list[RecognizerResult]:
        return [
            RecognizerResult(
                entity_type=str(result.type),
                start=result.start,
                end=result.end,
                score=result.score,
            )
            for result in analyzer_results
        ]

    def format_anonymized_operators(
        self,
        operators: dict[TextAnalyzerType, type[Operator]],
        engine: AnonymizerEngine,
    ) -> dict[str, OperatorConfig]:
        results = {}

        for k, v in operators.items():
            engine.add_anonymizer(v)
            results[k] = OperatorConfig(v().operator_name(), {})

        return results

    async def anonymize(
        self,
        text: str,
        analyzer_results: list[TextAnalyzedResult],
        operators: dict[TextAnalyzerType, type[Operator]],
    ) -> TextAnonymizedResult:
        engine = AnonymizerEngine()

        if len(analyzer_results) == 0:
            return TextAnonymizedResult(text=text, items=[])

        result = engine.anonymize(
            text=text,
            analyzer_results=self.format_recognizer_results(analyzer_results),
            operators=self.format_anonymized_operators(operators, engine),
        )

        return TextAnonymizedResult(
            text=result.text,
            items=[
                TextAnonymizedResultItem(
                    start=item.start,
                    end=item.end,
                    entity_type=item.entity_type,
                    text=item.text,
                    operator=item.operator,
                )
                for item in result.items
            ],
        )
