"""
Generates a test suite (unit tests) for the implemented code.
"""
from .llm_clients import openai_chat_completion
from .config import TEST_GENERATOR_MODEL

TEST_GEN_PROMPT_TEMPLATE = """
You are a test generator. The user has implemented the following code:

{code}

pgsql
Copy
Edit

Your job is to generate Python unit tests using pytest that thoroughly test the functionality.
Include both typical cases and edge cases. Make sure the tests are comprehensive.
Return only the test code, do not add extra commentary.
"""

def generate_tests(code: str) -> str:
    """
    Generates pytest-based test code as a string.
    """
    prompt = TEST_GEN_PROMPT_TEMPLATE.format(code=code)
    test_code = openai_chat_completion(
        prompt=prompt,
        model=TEST_GENERATOR_MODEL
    )
    return test_code