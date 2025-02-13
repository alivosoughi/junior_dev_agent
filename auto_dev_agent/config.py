"""
Configuration settings for the Automated Developer Agent.
"""
import os

# Example: load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR-OPENAI-API-KEY")

# Alternatively, you might store model names, prompts, or other settings here.
PLANNER_MODEL = "gpt-3.5-turbo"         # LLM for planning
CODE_GENERATOR_MODEL = "gpt-3.5-turbo"  # LLM for code generation
TEST_GENERATOR_MODEL = "gpt-3.5-turbo"  # LLM for test generation
REFINEMENT_MODEL = "gpt-3.5-turbo"      # LLM for refinement

# Additional configuration for e.g. test coverage thresholds
COVERAGE_THRESHOLD = 80  # in percent
