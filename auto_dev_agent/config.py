"""
Configuration settings for the Automated Developer Agent.
"""
import os
import json


with open("./api.json", "r") as file:
    api_key = json.load(file)['api_key']

# Example: load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", api_key)

# Alternatively, you might store model names, prompts, or other settings here.
PLANNER_MODEL = "gpt-4o-mini"         # LLM for planning
CODE_GENERATOR_MODEL = "gpt-4o-mini"  # LLM for code generation
TEST_GENERATOR_MODEL = "gpt-4o-mini"  # LLM for test generation
REFINEMENT_MODEL = "gpt-4o-mini"      # LLM for refinement

# Additional configuration for e.g. test coverage thresholds
COVERAGE_THRESHOLD = 80  # in percent
