from pii_anonymizer.generators.phone_generator import PhoneGenerator


def test_credit_card_generator():
    generator = PhoneGenerator()
    text = "1 669 900 9000x123"
    params = {"entity_type": "PHONE_NUMBER"}
    generated = generator.operate(text, params)
    assert len(generated) > 0
