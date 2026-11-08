
from dataset_loader import load_test_dataset
from llm_client import generate_response


def execute_test_cases():
    test_cases = load_test_dataset()

    results = []

    for test_case in test_cases:
        test_id = test_case["test_id"]
        prompt = test_case["prompt"]
        expected_response = test_case["expected_response"]

        print(f"\nExecuting Test Case: {test_id}")
        print("Prompt:", prompt)

        try:
            actual_response = generate_response(prompt)

            result = {
                "test_id": test_id,
                "prompt": prompt,
                "expected_response": expected_response,
                "actual_response": actual_response,
                "status": "EXECUTED"
            }

            results.append(result)

            print("Actual Response:", actual_response)
            print("Status: EXECUTED")

        except Exception as error:
            print("Execution Failed:", error)

            results.append({
                "test_id": test_id,
                "prompt": prompt,
                "expected_response": expected_response,
                "actual_response": "",
                "status": "ERROR"
            })

    return results


if __name__ == "__main__":
    execution_results = execute_test_cases()

    print("\nExecution Summary")
    print("Total Test Cases:", len(execution_results))
    print(
        "Successfully Executed:",
        sum(
            result["status"] == "EXECUTED"
            for result in execution_results
        )
    )
    print(
        "Execution Errors:",
        sum(
            result["status"] == "ERROR"
            for result in execution_results
        )
    )
