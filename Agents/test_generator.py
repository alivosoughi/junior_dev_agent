# Please install OpenAI SDK first: `pip3 install openai`
import re
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

def test_generator(function_description, funftion_signiture, function_location):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a unit Test generator. you are given the location of function file relative to this test file. When you answer, output your response as a valid JSON "
                "object with two keys: first, 'code' whose value is the Python unit Test code for the given function. if all cases pass return true, if not return false. second, 'class_name' whose value is the name of test class. Do not include any "
                "explanation, markdown formatting, or extra text."},
            {
                "role": "user",
                "content": "I implemented a function in location: '" + function_location + "', and the root directory is junior_dev_agent with the following description: \n" +function_description +"\n and the following signiture: " + funftion_signiture + "\n I want you to only write test cases for this function and check all critical test cases in python. only return the python code"
            }
        ]
    )
    response = completion.choices[0].message.content

    try:
        result = json.loads(response)
        python_code = result.get("code", "")
        name = result.get("class_name", "")
    except json.JSONDecodeError:
        print("Failed to decode JSON. Here is the raw output:")
        python_code = response
    destination = 'outputs/tests/' + name + '.py'
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # junior_dev_agent/
    destination = os.path.abspath(os.path.join(project_root, destination))
    with open(destination, "w") as file:
        file.write(python_code)

    return destination


