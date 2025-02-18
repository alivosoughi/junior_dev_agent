# Automated Developer Agent

This repository contains a Python-based software system that emulates a "junior developer" workflow:

1. Receives a task (function/algorithm to implement).
2. Plans and writes an initial implementation.
3. Generates a suite of tests.
4. Runs and analyzes test results.
5. Refines the code based on feedback.
6. Iterates until the code meets quality standards.

## Features

- **Planner / Task Interpreter**: Breaks down user requirements.
- **Code Generator**: Uses an LLM (e.g., OpenAI GPT) to produce initial code.
- **Test Generator**: Creates test cases with coverage for typical and edge scenarios.
- **Test Runner**: Executes tests, collects results, coverage, and performance metrics.
- **Result Interpreter**: Analyzes test failures, logs, and output to provide feedback.
- **Refinement Module**: Iteratively improves the code based on feedback.

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/automated-developer-agent.git
    ```
2. Install dependencies:
    ```bash
    cd automated-developer-agent
    pip install -r requirements.txt
    ```
3. Set up your environment variables for LLM usage (e.g., `OPENAI_API_KEY`).

## Usage

To run the automated developer agent, simply execute:
```bash
python main.py
    