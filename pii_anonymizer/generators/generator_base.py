from faker import Faker
from presidio_anonymizer.operators import Operator, OperatorType


class GeneratorBase(Operator):
    def __init__(self):
        self.faker = Faker()

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params: dict | None = None) -> None:
        pass

    def operator_name(self) -> str:
        return self.__class__.__name__
