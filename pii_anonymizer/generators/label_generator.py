from pii_anonymizer.generators.generator_remember_base import GeneratorRememberBase


class LabelGenerator(GeneratorRememberBase):
    remember_values: dict[str, dict[str, str]] = {}

    def _get_cache(self) -> dict[str, dict[str, str]]:
        return LabelGenerator.remember_values

    def _generate(self, text: str, params: dict, entity_type: str) -> str:
        counter = params.get("counter", 0)
        counter += 1
        params["counter"] = counter
        return f"<{entity_type.lower()}_{counter}>"
