
import json
from pathlib import Path


def load_test_dataset():
    file_path = Path(__file__).parent / "test_dataset.json"

    with open(file_path, "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    if not isinstance(test_cases, list):
        raise ValueError("Test dataset must be a list")

    if not test_cases:
        raise ValueError("Test dataset cannot be empty")

    for test_case in test_cases:
        required_fields = ["test_id", "prompt", "expected_response"]

        for field in required_fields:
            if field not in test_case:
                raise ValueError(
                    f"Missing required field: {field}"
                )

    return test_cases


if __name__ == "__main__":
    dataset = load_test_dataset()

    print("Dataset loaded successfully!")
    print("Total Test Cases:", len(dataset))

    for test_case in dataset:
        print(
            test_case["test_id"],
            "|",
            test_case["prompt"]
        )
