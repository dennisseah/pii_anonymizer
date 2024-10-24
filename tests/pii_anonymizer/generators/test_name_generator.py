from pii_anonymizer.generators.name_generator import NameGenerator


def test_name_generator():
    generator = NameGenerator()
    text = "John Doe"
    params = {"entity_type": "PERSON"}
    generated = generator.operate(text, params)
    assert len(generated) > 0
