from pii_anonymizer.generators.mask_generator import MaskGenerator


def test_mask_generator():
    generator = MaskGenerator()
    text = "John Doe"
    params = {}
    generated = generator.operate(text, params)
    assert generated == "********"


def test_mask_generator_with_X():
    MaskGenerator.mask_char_mapping = {"PERSON": "X"}
    generator = MaskGenerator()
    text = "John Doe"
    params = {"entity_type": "PERSON"}
    generated = generator.operate(text, params)
    assert generated == "XXXXXXXX"
