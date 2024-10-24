from pii_anonymizer.generators.generator_base import GeneratorBase


class PhoneGenerator(GeneratorBase):
    def operate(self, text: str, params: dict | None = None) -> str:
        return self.faker.phone_number()
