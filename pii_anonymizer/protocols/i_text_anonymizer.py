from typing import Protocol

from presidio_anonymizer.operators import Operator

from pii_anonymizer.models.text_analyzed_result import (
    TextAnalyzedResult,
    TextAnalyzerType,
)
from pii_anonymizer.models.text_anonymized_result import TextAnonymizedResult


class ITextAnonymizer(Protocol):
    """Protocol for Text Anonymizer Service."""

    async def anonymize(
        self,
        text: str,
        analyzer_results: list[TextAnalyzedResult],
        operators: dict[TextAnalyzerType, type[Operator]],
    ) -> TextAnonymizedResult:
        """
        Anonymize the text based on the analyzed results.

        :param text : The text to anonymize.
        :param analyzer_results : The analyzed results.
        :param operators : The operators to use for anonymization.
        :return : The anonymized result.
        """
        ...
