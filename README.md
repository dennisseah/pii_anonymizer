# Introduction

PII Anonymizer is a service that anonymizes the PII data in the text.

## Prerequisites

- python 3.12
- install poetry (https://python-poetry.org/docs/)
- install vscode (https://code.visualstudio.com/)

## Setup

1. Clone the repository
2. `cd PIIAnonymizer` (root directory of this git repository)
3. `python -m venv .venv`
4. `poetry install` (install the dependencies)
5. `python -m spacy download en_core_web_lg` (download the spacy model)
6. code . (open the project in vscode)
7. install the recommended extensions (cmd + shift + p -> `Extensions: Show Recommended Extensions`)
8. `pre-commit install` (install the pre-commit hooks)

## Features

- &check; Identify and anonymize Name entities either by replace it 
  - with a label (e.g. <person_1>),
  - masking it with a mask (e.g. ****) or
  - with a fake name.
- &check; Identify and anonymize Phone entities either by replace it
  - with a label (e.g. <phone_number_1>),
  - masking it with a mask (e.g. ****) or
  - with a fake number.
- &check; Identify and anonymize credit card entities either by replace it
  - with a label (e.g. <credit_card_1>),
  - masking it with a mask (e.g. ****)
  - or with a fake number.
- &check; Same entity should be anonymized consistently throughout the text.
- &check; Random generator can be seeded for reproducibility.

## Sample Usage

Run the `main.py` in samples module.

```python
python -m samples.main
```

```
Original text:
Her name is Mary Ann. My name is James Bond. My phone number is 212-555-5555.
My credit card is 5548364515335857. Again my name is James Bond and number is
212-555-5555.
```

```
Anonymized text:
Her name is Monique Hamilton. My name is Jesse Townsend. My phone number is <phone_number_1>.
My credit card is XXXXXXXXXXXXXXXX. Again my name is Jesse Townsend and number is
<phone_number_1>.
```


## Unit Test Coverage

```sh
python -m pytest -p no:warnings --cov-report term-missing --cov=pii_anonymizer tests
```
