
from baseline_loader import load_baseline
from llm_client import generate_response
from similarity_checker import calculate_similarity


SIMILARITY_THRESHOLD = 0.75


def run_regression():

    baseline = load_baseline()
    results = []

    for test_case in baseline:

        test_id = test_case["test_id"]
        prompt = test_case["prompt"]
        baseline_response = test_case["baseline_response"]

        print(f"\nExecuting Regression Test: {test_id}")

        try:
            actual_response = generate_response(prompt)

            # TEMPORARY: Simulate a regression failure
            if test_id == "TC_001":
                actual_response = (
                    "The Earth revolves around the Sun "
                    "and takes approximately 365 days."
                )


            similarity_score = calculate_similarity(
                baseline_response,
                actual_response
            )

            status = (
                "PASS"
                if similarity_score >= SIMILARITY_THRESHOLD
                else "FAIL"
            )

            results.append({
                "test_id": test_id,
                "similarity_score": round(similarity_score, 4),
                "status": status
            })

            print("Similarity Score:", round(similarity_score, 4))
            print("Status:", status)

        except Exception as error:

            print("Regression Test Error:", error)

            results.append({
                "test_id": test_id,
                "similarity_score": None,
                "status": "ERROR"
            })

    return results


if __name__ == "__main__":

    results = run_regression()

    print("\nRegression Test Summary")
    print("Total Tests:", len(results))
    print("Passed:", sum(r["status"] == "PASS" for r in results))
    print("Failed:", sum(r["status"] == "FAIL" for r in results))
    print("Errors:", sum(r["status"] == "ERROR" for r in results))
