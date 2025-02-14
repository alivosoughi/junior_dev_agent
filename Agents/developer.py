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


def developer(language, funtion_description):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a code generator. When you answer, output your response as a valid JSON "
                "object with two keys, first: 'code' whose value is the Python code. second: 'signiture' whose value is the function signiture including function name, inputs and types, and output and type. Do not include any "
                "explanation, markdown formatting, or extra text."},
            {
                "role": "user",
                "content": "generate a code in" + language + " to implement following function discription: \n" + funtion_description
            }
        ]
    )
    response = completion.choices[0].message.content

    try:
        result = json.loads(response)
        python_code = result.get("code", "")
        function_signiture = result.get("signiture", "")
        funtion_name = function_signiture.split(" ")[1].split("(")[0]
        destination = 'outputs/functions/' + funtion_name + '.py'
    except json.JSONDecodeError:
        print("Failed to decode JSON. Here is the raw output:")
        python_code = response
    
    
    destination = os.path.abspath(os.path.join(project_root, destination))

    with open(destination, "w") as file:
        file.write(python_code)

    return (function_signiture, funtion_description, destination)

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))