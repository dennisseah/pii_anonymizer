from pii_anonymizer.generators.ip_address_generator import IPAddressGenerator


def test_credit_card_generator():
    generator = IPAddressGenerator()
    text = "128.0.1.1"
    params = {"entity_type": "IP_ADDRESS"}
    generated = generator.operate(text, params)
    assert len(generated) > 0
