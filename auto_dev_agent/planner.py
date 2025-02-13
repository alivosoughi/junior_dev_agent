"""
Planner/Task Interpreter module.
Breaks down a high-level specification into an actionable plan.
"""
from .llm_clients import openai_chat_completion
from .config import PLANNER_MODEL

PLANNER_PROMPT_TEMPLATE = """
You are a planning assistant. The user has the following task:
"{task}"

1. Interpret the user's requirement.
2. Break down the requirement into subtasks.
3. Outline a method or pseudocode for the solution.

Provide a structured plan/pseudocode.
"""

def plan_task(task_spec: str) -> str:
    """
    Uses an LLM to generate a plan for the given task specification.
    Returns the plan as a string.
    """
    prompt = PLANNER_PROMPT_TEMPLATE.format(task=task_spec)
    plan = openai_chat_completion(
        prompt=prompt,
        model=PLANNER_MODEL
    )
    return plan
