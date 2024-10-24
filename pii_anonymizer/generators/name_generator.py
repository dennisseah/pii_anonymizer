from pii_anonymizer.generators.generator_remember_base import GeneratorRememberBase


class NameGenerator(GeneratorRememberBase):
    remember_values: dict[str, dict[str, str]] = {}

    def _get_cache(self) -> dict[str, dict[str, str]]:
        return NameGenerator.remember_values

    def _generate(self, text: str, params: dict, entity_type: str) -> str:
        return self.faker.name()
