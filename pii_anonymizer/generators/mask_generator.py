from pii_anonymizer.generators.generator_base import GeneratorBase


class MaskGenerator(GeneratorBase):
    mask_char_mapping = {}
    default_mask_char = "*"

    def operate(self, text: str, params: dict | None = None) -> str:
        entity_type = params.get("entity_type") if params is not None else None

        chars = (
            MaskGenerator.mask_char_mapping.get(
                entity_type, MaskGenerator.default_mask_char
            )
            if entity_type is not None
            else MaskGenerator.default_mask_char
        )

        return chars * len(text)
