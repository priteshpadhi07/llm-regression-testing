
# LLM Regression Testing Framework

An automated LLM regression testing framework developed using Python, Pytest, Ollama, and Sentence Transformers.

## Features

- Local LLM integration using Ollama Llama 3.2
- JSON-based test dataset
- Baseline response generation and validation
- Semantic similarity comparison
- Automated regression detection
- Expected response validation
- LLM response consistency testing
- Negative test scenarios
- Pytest integration
- HTML regression reports

## Technologies

- Python
- Pytest
- Ollama (Llama 3.2)
- Sentence Transformers
- Requests
- pytest-html

## Prerequisites

Install Ollama and download the model:

```bash
ollama pull llama3.2
```

Ensure the Ollama server is running.

## Installation

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## Generate Baseline

```bash
python baseline_manager.py
```

Review the generated baseline before using it as a trusted reference.

## Run Regression Tests

```bash
python -m pytest test_llm_regression.py -v -s
```

## Generate HTML Report

```bash
python -m pytest test_llm_regression.py -v -s --html=regression_report.html --self-contained-html
```

## Additional Validation

Expected response validation:

```bash
python response_validator.py
```

Consistency testing:

```bash
python consistency_checker.py
```

Negative testing:

```bash
python negative_test_checker.py
```

## Limitations

- Semantic similarity does not guarantee factual correctness.
- Similarity thresholds require calibration.
- Baseline responses must be reviewed.
- LLM output may vary across executions.
