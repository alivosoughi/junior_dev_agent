"""
Provides functions/classes to interact with various LLM providers (OpenAI, Anthropic, etc.).
"""

import openai
from .config import OPENAI_API_KEY

# Create an OpenAI client instance
client = openai.OpenAI(api_key=OPENAI_API_KEY)


def openai_chat_completion(prompt, model="gpt-4o-mini", temperature=0.0, max_tokens=1024):
    """
    Calls the OpenAI ChatCompletion endpoint with the given prompt.

    Args:
        prompt (str): The input prompt for the model.
        model (str): The LLM model to use (default: "gpt-4o-mini").
        temperature (float): Sampling temperature (0.0 means deterministic output).
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: The generated response from the model.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except openai.APIError as api_err:
        print(f"OpenAI API error: {api_err}")
    except openai.RateLimitError:
        print("OpenAI API rate limit exceeded. Try again later.")
    except openai.AuthenticationError:
        print("Invalid OpenAI API key. Please check your credentials.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return None  # Return None in case of failure

# Similarly, you can define other LLM client functions if you want to use multiple providers
