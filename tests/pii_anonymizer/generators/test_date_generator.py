from pytest_mock import MockerFixture

from pii_anonymizer.generators.datetime_generator import DateTimeGenerator


def test_datetime_generator_date():
    generator = DateTimeGenerator()
    text = "2022-10-01"
    params = {"entity_type": "DATE_TIME"}
    generated = generator.operate(text, params)
    assert len(generated) == 10


def test_datetime_generator_datetime():
    generator = DateTimeGenerator()
    text = "2022-10-01T13:00:00"
    params = {"entity_type": "DATE_TIME"}
    generated = generator.operate(text, params)
    assert len(generated) == 19


def test_datetime_generator_datetime_dateparser_return_none(mocker: MockerFixture):
    mocker.patch("dateparser.parse", return_value=None)

    generator = DateTimeGenerator()
    text = "2022-10-01T13:00:00"
    params = {"entity_type": "DATE_TIME"}
    generated = generator.operate(text, params)
    assert len(generated) == 19


def test_datetime_generator_datetime_dateparser_raise_exception(mocker: MockerFixture):
    mocker.patch("dateparser.parse", side_effect=Exception)

    generator = DateTimeGenerator()
    text = "2022-10-01"
    params = {"entity_type": "DATE_TIME"}
    generated = generator.operate(text, params)
    assert len(generated) == 10
