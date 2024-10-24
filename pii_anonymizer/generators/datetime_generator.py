import datetime
import random

import dateparser

from pii_anonymizer.generators.generator_base import GeneratorBase


class DateTimeGenerator(GeneratorBase):
    date_range = 10

    def parse_datetime(self, text: str) -> str | None:
        try:
            d = dateparser.parse(text)

            if d is None:
                return None

            result = d + datetime.timedelta(
                days=random.randrange(-self.date_range, self.date_range)
            )

            return (
                result.strftime("%Y-%m-%d")
                if len(text) < 12
                else result.strftime("%Y-%m-%d %H:%M:%S")
            )

        except Exception:
            return None

    def operate(self, text: str, params: dict | None = None) -> str:
        parsed_date = self.parse_datetime(text)
        if parsed_date is not None:
            return parsed_date

        if len(text) < 12:
            return str(self.faker.past_date())

        fake_date = str(self.faker.past_datetime())
        idx = fake_date.find(".")
        if idx != -1:
            fake_date = fake_date[:idx]

        return fake_date
