
from similarity_checker import calculate_similarity


SIMILARITY_THRESHOLD = 0.75


def run_negative_tests():

    test_cases = [
        {
            "test_id": "NEG_001",
            "expected": "Regression testing checks that software changes do not introduce new defects.",
            "actual": "The capital of France is Paris."
        },
        {
            "test_id": "NEG_002",
            "expected": "Smoke testing verifies the critical functionality of a software build.",
            "actual": "Python is a programming language used for automation."
        },
        {
            "test_id": "NEG_003",
            "expected": "API testing validates application programming interfaces.",
            "actual": "The Earth revolves around the Sun."
        }
    ]

    passed = 0
    failed = 0

    for test_case in test_cases:

        score = calculate_similarity(
            test_case["expected"],
            test_case["actual"]
        )

        # Negative test passes when an unrelated answer is rejected
        status = (
            "PASS"
            if score < SIMILARITY_THRESHOLD
            else "FAIL"
        )

        if status == "PASS":
            passed += 1
        else:
            failed += 1

        print("\nTest Case:", test_case["test_id"])
        print("Similarity Score:", round(score, 4))
        print("Status:", status)

    print("\nNegative Test Summary")
    print("Total Tests:", len(test_cases))
    print("Passed:", passed)
    print("Failed:", failed)


if __name__ == "__main__":
    run_negative_tests()
