from pydantic import BaseModel


class TextAnonymizedResultItem(BaseModel):
    start: int
    end: int
    entity_type: str
    text: str
    operator: str


class TextAnonymizedResult(BaseModel):
    text: str
    items: list[TextAnonymizedResultItem]
