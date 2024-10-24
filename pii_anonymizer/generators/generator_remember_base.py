from pii_anonymizer.generators.generator_base import GeneratorBase


class GeneratorRememberBase(GeneratorBase):
    def _generate(self, text: str, params: dict, entity_type: str) -> str: ...

    def _get_cache(self) -> dict[str, dict[str, str]]: ...

    def operate(self, text: str, params: dict | None = None) -> str:
        if params is None:
            raise ValueError("entity_type is required")

        entity_type = params.get("entity_type")
        if entity_type is None:
            raise ValueError("entity_type is required")

        cache = self._get_cache()
        # if the text has been seen before, return the same value
        if entity_type in cache and text in cache[entity_type]:
            return cache[entity_type][text]

        val = self._generate(text, params, entity_type)

        # remember the value
        if entity_type not in cache:
            cache[entity_type] = {}
        cache[entity_type][text] = val

        return val
