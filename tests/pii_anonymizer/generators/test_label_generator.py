import pytest

from pii_anonymizer.generators.label_generator import LabelGenerator

# def test_label_generator():
#     generator = LabelGenerator()
#     text = "John Doe"
#     params = {"entity_type": "PERSON"}
#     generated = generator.operate(text, params)
#     assert generated == "<person_1>"


def test_label_generator_multiple():
    generator = LabelGenerator()
    params = {"entity_type": "PERSON"}
    generated = generator.operate("John Doe", params)
    assert generated == "<person_1>"

    generated = generator.operate("Mary Jane", params)
    assert generated == "<person_2>"


def test_label_generator_no_entity_type():
    generator = LabelGenerator()
    text = "John Doe"

    with pytest.raises(ValueError, match="entity_type is required"):
        generator.operate(text, {})


def test_label_generator_no_params():
    generator = LabelGenerator()
    text = "John Doe"

    with pytest.raises(ValueError, match="entity_type is required"):
        generator.operate(text)
