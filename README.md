# From Git to Gold – FreshCart Pipelines

A Data Engineering assignment covering Git, CI/CD,
ELT pipelines, Machine Learning and Stream Processing.

## Project Modules

### Part A – Git and CI/CD
GitHub repository management and automated testing
using GitHub Actions and pytest.

### Part B – FreshCart ELT
Data ingestion, cleaning, validation, deduplication,
SCD Type 2 and Gold-layer transformations using Snowflake.

### Part C – Machine Learning
Iris classification pipeline using Mage AI.

### Part D – Stream Processing
Food-order event streaming using Python and RabbitMQ.

### Part E – Final Report
Documentation, integration diagram and viva preparation.

## Project Structure

- elt/ : FreshCart ELT pipeline
- iris_project/ : Mage ML pipeline
- stream/ : RabbitMQ dispatcher and driver
- tests/ : Automated Python tests
- .github/workflows/ : GitHub Actions CI

## Technologies

- Python
- SQL
- Git and GitHub
- Snowflake
- Mage AI
- RabbitMQ
- Pytest
- GitHub Actions

## Development and Validation

### Setup
Install project dependencies:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

### Run tests

    pytest -v

### Project folders
- elt/: FreshCart ELT notebook
- iris_project/: Iris ML project
- stream/: RabbitMQ dispatcher and driver
- tests/: Automated tests
- .github/workflows/: GitHub Actions CI
