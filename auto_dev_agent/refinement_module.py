"""
Uses feedback to refine or modify the code and/or test suite.
"""
from .llm_clients import openai_chat_completion
from .config import REFINEMENT_MODEL

REFINE_CODE_PROMPT_TEMPLATE = """
You are a code refiner. The current code is:

{code}

python
Copy
Edit

We have received this feedback:
"{feedback}"

Please suggest an improved version of the code in Python. Provide only the code.
"""

REFINE_TESTS_PROMPT_TEMPLATE = """
You are a test refiner. The current test code is:

{test_code}

python
Copy
Edit

We have received this feedback:
"{feedback}"

Please suggest an improved version of the test code in Python. Provide only the code.
"""

def refine_code(code: str, feedback: str) -> str:
    """
    Uses an LLM to refine/improve the code based on feedback.
    """
    prompt = REFINE_CODE_PROMPT_TEMPLATE.format(code=code, feedback=feedback)
    refined_code = openai_chat_completion(
        prompt=prompt,
        model=REFINEMENT_MODEL
    )
    return refined_code

def refine_tests(test_code: str, feedback: str) -> str:
    """
    Uses an LLM to refine/improve the test code based on feedback.
    """
    prompt = REFINE_TESTS_PROMPT_TEMPLATE.format(test_code=test_code, feedback=feedback)
    refined_test_code = openai_chat_completion(
        prompt=prompt,
        model=REFINEMENT_MODEL
    )
    return refined_test_code