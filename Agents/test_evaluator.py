import subprocess
import sys
import json
import re

def run_tests(test_file):
    """
    Runs unit tests from the given test_file in a fresh subprocess.
    
    Returns a dictionary with the test results:
        {
            "tests_run": <number of tests run>,
            "failures": <number of failures>,
            "errors": <number of errors>,
            "success": <True if all tests passed, else False>,
            "output": <full output from the test run>
        }
    """
    # This code snippet (as a string) will be executed in a new Python process.
    # It dynamically loads the test file (without importing it into our main process),
    # runs the tests using unittest, and then prints the test results in JSON between
    # special markers.
    test_runner_code = f"""
import unittest
import importlib.util
import json
import sys

# Dynamically load the test module from the given file
spec = importlib.util.spec_from_file_location("temp_test_module", r"{test_file}")
test_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_module)

# Load tests from the module
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_module)

# Run the tests and capture the results
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Prepare the results dictionary
results = {{
    "tests_run": result.testsRun,
    "failures": len(result.failures),
    "errors": len(result.errors),
    "success": result.wasSuccessful()
}}

# Print JSON result with markers for easy extraction
print("<<JSON_START>>")
print(json.dumps(results))
print("<<JSON_END>>")
"""
    # Run the above code in a new subprocess using the same Python interpreter.
    proc = subprocess.run(
        [sys.executable, "-c", test_runner_code],
        capture_output=True,
        text=True
    )
    
    # Combine stdout and stderr output
    full_output = proc.stdout + proc.stderr

    # Use a regex to extract the JSON block between our markers.
    match = re.search(r"<<JSON_START>>(.*?)<<JSON_END>>", full_output, re.DOTALL)
    if match:
        json_str = match.group(1).strip()
        try:
            test_results = json.loads(json_str)
        except json.JSONDecodeError:
            test_results = {
                "tests_run": 0,
                "failures": 0,
                "errors": 0,
                "success": False
            }
    else:
        # If we couldn't find the JSON block, assume something went wrong.
        test_results = {
            "tests_run": 0,
            "failures": 0,
            "errors": 0,
            "success": False
        }
    
    # Add the full captured output to the results dictionary.
    test_results["output"] = full_output
    return test_results
