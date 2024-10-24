"""Defines our top level DI container.
Utilizes the Lagom library for dependency injection, see more at:

- https://lagom-di.readthedocs.io/en/latest/
- https://github.com/meadsteve/lagom
"""

import logging

from dotenv import load_dotenv
from lagom import Container, dependency_definition

from pii_anonymizer.protocols.i_text_analyzer import ITextAnalyzer
from pii_anonymizer.protocols.i_text_anonymizer import ITextAnonymizer

load_dotenv(dotenv_path=".env")


container = Container()
"""The top level DI container for our application."""


# Register our dependencies ------------------------------------------------------------


@dependency_definition(container, singleton=True)
def _() -> logging.Logger:
    return logging.getLogger("pii_anonymizer")


@dependency_definition(container, singleton=True)
def _(c: Container) -> ITextAnalyzer:
    from pii_anonymizer.services.presidio_text_analyzer import PresidioTextAnalyzer

    return c[PresidioTextAnalyzer]


@dependency_definition(container, singleton=True)
def _(c: Container) -> ITextAnonymizer:
    from pii_anonymizer.services.presidio_text_anonymizer import PresidioTextAnonymizer

    return c[PresidioTextAnonymizer]
