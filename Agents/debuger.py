# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
import json
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # junior_dev_agent/
apikeys_path = os.path.join(project_root, "api_keys.json")
with open(apikeys_path, "r") as file:
    apis = json.load(file)

# Access an API's URL and key
deepSeek_url = apis["deepseek"]["url"]
deepSeek_key = apis["deepseek"]["key"]
openai_url = apis["openai"]["url"]
openai_key = apis["openai"]["key"]

client = OpenAI(api_key = openai_key)


def debuger(code_location, error):
    with open(code_location, "r", encoding="utf-8") as file:
        code = file.read()  # Read the entire file into a variable

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a code debuger. When you answer, output your response as a valid JSON "
                "object with only one key, 'code' whose value is the Python code. you get a prompt including a code and it's error after run, and you will debug the code and return the debuged code. Do not include any "
                "explanation, markdown formatting, or extra text."},
            {
                "role": "user",
                "content": "here is my code:\n'\n" + code + "\n'\n and here is the error: \n'\n" + error + "\n'\n I want you to debug the code and return the debuged code"
            }
        ]
    )
    response = completion.choices[0].message.content

    try:
        result = json.loads(response)
        python_code = result.get("code", "")
    except json.JSONDecodeError:
        print("Failed to decode JSON. Here is the raw output:")
        python_code = response
    
    with open(code_location, "w") as file:
        file.write(python_code)
