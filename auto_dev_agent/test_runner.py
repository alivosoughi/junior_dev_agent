"""
Runs the tests for the generated code. Collects results, coverage, etc.
"""
import os
import subprocess
import tempfile

def run_tests_and_collect_results(code: str, test_code: str) -> dict:
    """
    Runs the given test code against the provided code in a temporary
    environment. Returns a dictionary with test pass/fail results,
    coverage info, error messages, etc.
    """
    results = {
        "passed": False,
        "num_tests": 0,
        "num_failures": 0,
        "failures_detail": [],
        "coverage": 0.0,
        "output": ""
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        # Save the code and test files in temp dir
        code_file_path = os.path.join(tmpdir, "solution.py")
        test_file_path = os.path.join(tmpdir, "test_solution.py")

        with open(code_file_path, "w") as f:
            f.write(code)

        with open(test_file_path, "w") as f:
            f.write(test_code)

        # Optionally run coverage
        # We could use 'pytest --cov=.' or manually run coverage
        try:
            cmd = ["pytest", "--cov=.", "--cov-report=term-missing", tmpdir]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()

            results["output"] = stdout + "\n" + stderr
            if "failed" not in stdout.lower() and "error" not in stdout.lower():
                results["passed"] = True

            # Simple parse for # of tests run
            # e.g. "collected X items"
            for line in stdout.split("\n"):
                if line.strip().startswith("collected"):
                    parts = line.split()
                    if len(parts) >= 2:
                        results["num_tests"] = int(parts[1])
                if "failed," in line or "failed" in line and "x" in line:
                    # e.g. "=== 1 failed, 2 passed in 0.05s ==="
                    # parse the line carefully
                    pass  # You can parse deeper if needed

            # Extract coverage if present
            for line in stdout.split("\n"):
                if "TOTAL" in line and "%" in line:
                    # e.g. "TOTAL      10      2    80%"
                    coverage_str = line.split()[-1]  # e.g. "80%"
                    coverage_str = coverage_str.replace("%", "")
                    results["coverage"] = float(coverage_str)

        except Exception as e:
            results["output"] = f"Error running tests: {e}"

    return results
