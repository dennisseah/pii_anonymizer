from typing import Literal

from pydantic import BaseModel

TextAnalyzerType = Literal["PERSON", "PHONE_NUMBER", "CREDIT_CARD"]


class TextAnalyzedResult(BaseModel):
    type: TextAnalyzerType
    start: int
    end: int
    score: float
