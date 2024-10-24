from pii_anonymizer.generators.generator_base import GeneratorBase


class EmailGenerator(GeneratorBase):
    def operate(self, text: str, params: dict | None = None) -> str:
        return self.faker.email()
