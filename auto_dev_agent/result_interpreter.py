"""
Interprets the test results and provides feedback for refinement.
"""
FEEDBACK_TEMPLATE = """
The following test results were obtained:

Output:
{output}

Based on these results, describe:
1. The likely causes of any failures or errors.
2. Potential improvements or fixes that can be made to the code.
Be concise but specific.
"""

from .llm_clients import openai_chat_completion
from .config import REFINEMENT_MODEL

def interpret_test_results(test_results: dict) -> str:
    """
    Takes the results dictionary from the test runner and uses an LLM to interpret
    failures and recommend fixes.
    """
    if test_results["passed"] and test_results["coverage"] >= 80:
        return "All tests passed with sufficient coverage. Looks good!"

    prompt = FEEDBACK_TEMPLATE.format(output=test_results["output"])
    feedback = openai_chat_completion(
        prompt=prompt,
        model=REFINEMENT_MODEL
    )
    return feedback
