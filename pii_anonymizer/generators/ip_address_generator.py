from pii_anonymizer.generators.generator_base import GeneratorBase


class IPAddressGenerator(GeneratorBase):
    def operate(self, text: str, params: dict | None = None) -> str:
        return self.faker.ipv4()