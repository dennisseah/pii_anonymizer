from pii_anonymizer.generators.email_generator import EmailGenerator


def test_credit_card_generator():
    generator = EmailGenerator()
    text = "tester@company.org"
    params = {"entity_type": "EMAIL_ADDRESS"}
    generated = generator.operate(text, params)
    assert len(generated) > 0
