"""
Module to generate initial code from a plan/pseudocode.
"""
from .llm_clients import openai_chat_completion
from .config import CODE_GENERATOR_MODEL

CODE_GEN_PROMPT_TEMPLATE = """
You are a code generator. Based on the following plan:

Plan/Pseudocode:
"{plan}"

Generate clean, well-documented Python code that implements this plan. 
Include function definitions and docstrings. 
"""

def generate_code_from_plan(plan: str) -> str:
    """
    Generates Python code from the given plan/pseudocode.
    Returns a string containing Python code.
    """
    prompt = CODE_GEN_PROMPT_TEMPLATE.format(plan=plan)
    code = openai_chat_completion(
        prompt=prompt,
        model=CODE_GENERATOR_MODEL
    )
    return code
