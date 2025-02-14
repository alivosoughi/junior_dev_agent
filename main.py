from Agents.developer import developer
from Agents.test_generator import test_generator
from Agents.test_evaluator import run_tests
from Agents.debuger import debuger
import time

def main():
    programing_language = input("language: ")
    user_prompt = input("function description: ")
    res = developer(programing_language, user_prompt)
    function_location = res[2]
    test_location = test_generator(user_prompt, res[0], function_location)
    print("Running tests...")
    test_results = run_tests(test_location)
    while(not test_results["success"]):
        #ToDo: check if tests are correct
        debuger(function_location, test_results["output"])
        print("Running tests...")
        test_results = run_tests(test_location)
        print(test_results)
    print("Success!")

if __name__ == "__main__":
    main()