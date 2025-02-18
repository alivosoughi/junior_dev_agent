"""
Orchestrates the entire iterative workflow: plan -> generate code -> generate tests -> run tests -> refine -> repeat.
"""
from .planner import plan_task
from .code_generator import generate_code_from_plan
from .test_generator import generate_tests
from .test_runner import run_tests_and_collect_results
from .result_interpreter import interpret_test_results
from .refinement_module import refine_code, refine_tests

class AutomatedDeveloperAgent:
    def __init__(self, max_iterations: int = 5):
        self.max_iterations = max_iterations

    def run(self, task_spec: str):
        """
        Given a task specification, run the entire automated developer loop
        until tests pass or we hit the maximum number of iterations.
        """
        # 1. Plan / Task Interpretation
        plan = plan_task(task_spec)
        print("====== PLAN / PSEUDOCODE ======")
        print(plan)

        # 2. Code Generation
        current_code = generate_code_from_plan(plan)
        print("====== INITIAL CODE ======")
        print(current_code)

        # 3. Test Generation
        current_test_code = generate_tests(current_code)
        print("====== GENERATED TESTS ======")
        print(current_test_code)

        for iteration in range(self.max_iterations):
            print(f"\n----- Iteration {iteration+1} -----")
            # 4. Test Execution
            test_results = run_tests_and_collect_results(current_code, current_test_code)
            print("Test Output:", test_results["output"])

            # 5. Interpret Results
            feedback = interpret_test_results(test_results)
            print("Feedback:", feedback)

            # Check if we passed
            if test_results["passed"] and test_results["coverage"] >= 80:
                print("All tests passed with sufficient coverage. Stopping iteration.")
                break

            # 6. Refinement
            # Possibly refine both code and tests if needed
            # For simplicity, let's always refine the code.
            refined_code = refine_code(current_code, feedback)
            if "def " in refined_code:
                current_code = refined_code

            # Optionally refine tests, if needed
            # (If there's a clear reason the tests themselves are incomplete or failing)
            refined_test_code = refine_tests(current_test_code, feedback)
            if "def test_" in refined_test_code:
                current_test_code = refined_test_code

        # End of loop
        # 7. Final Output (in a real system, we might finalize or push to git, etc.)
        print("====== FINAL CODE ======")
        print(current_code)
        print("====== FINAL TEST CODE ======")
        print(current_test_code)
        print("Execution complete.")
