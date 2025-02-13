"""
Provides functions/classes to interact with various LLM providers (OpenAI, Anthropic, etc.).
"""
import openai
from .config import OPENAI_API_KEY

# Set up OpenAI
openai.api_key = OPENAI_API_KEY

def openai_chat_completion(prompt, model="gpt-3.5-turbo", temperature=0.0, max_tokens=1024):
    """
    Calls the OpenAI ChatCompletion endpoint with the given prompt.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        content = response.choices[0].message.content
        return content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return None

# Similarly, you can define other LLM client functions if you want to use multiple providers
