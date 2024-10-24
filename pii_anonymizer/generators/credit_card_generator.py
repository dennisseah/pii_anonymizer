from pii_anonymizer.generators.generator_base import GeneratorBase


class CreditCardGenerator(GeneratorBase):
    def operate(self, text: str, params: dict | None = None) -> str:
        val = self.faker.credit_card_number()
        if params is not None:
            params[text] = val
        return val
