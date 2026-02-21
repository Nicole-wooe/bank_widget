## Testing

### Install dependencies

poetry install

### Run tests

poetry run pytest

### Run tests with coverage

poetry run pytest --cov=src --cov-report=term-missing --cov-report=html

### Coverage report

HTML coverage report is generated in the `htmlcov` directory.
Open `htmlcov/index.html` in your browser to see detailed coverage.
