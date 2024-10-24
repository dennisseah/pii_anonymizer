from presidio_anonymizer.operators import OperatorType

from pii_anonymizer.generators.credit_card_generator import CreditCardGenerator


def test_credit_card_generator():
    generator = CreditCardGenerator()
    text = "1234-5678-1234-5678"
    params = {}
    generated = generator.operate(text, params)
    assert params[text] == generated


def test_credit_card_generator_get_name():
    generator = CreditCardGenerator()
    assert generator.operator_name() == "CreditCardGenerator"


def test_credit_card_generator_validate():
    # no actions
    generator = CreditCardGenerator()
    generator.validate()


def test_credit_card_generator_operator_type():
    # no actions
    generator = CreditCardGenerator()
    assert generator.operator_type() == OperatorType.Anonymize
