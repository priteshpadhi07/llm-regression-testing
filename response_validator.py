
from dataset_loader import load_test_dataset
from llm_client import generate_response
from similarity_checker import calculate_similarity


SIMILARITY_THRESHOLD = 0.75


def validate_responses():

    test_cases = load_test_dataset()
    results = []

    for test_case in test_cases:

        test_id = test_case["test_id"]
        prompt = test_case["prompt"]
        expected_response = test_case["expected_response"]

        print(f"\nValidating Test Case: {test_id}")

        try:
            actual_response = generate_response(prompt)

            if test_id in ["TC_001", "TC_002"]:
                print("Expected Response:", expected_response)
                print("Actual Response:", actual_response)


            similarity_score = calculate_similarity(
                expected_response,
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

            print("Validation Error:", error)

            results.append({
                "test_id": test_id,
                "similarity_score": None,
                "status": "ERROR"
            })

    return results


if __name__ == "__main__":

    results = validate_responses()

    print("\nExpected Response Validation Summary")
    print("Total Tests:", len(results))
    print("Passed:", sum(r["status"] == "PASS" for r in results))
    print("Failed:", sum(r["status"] == "FAIL" for r in results))
    print("Errors:", sum(r["status"] == "ERROR" for r in results))
