
import json
from pathlib import Path

from dataset_loader import load_test_dataset


BASELINE_FILE = Path(__file__).parent / "baseline_responses.json"


def load_baseline():
    with open(BASELINE_FILE, "r", encoding="utf-8") as file:
        baseline = json.load(file)

    if not isinstance(baseline, list) or not baseline:
        raise ValueError("Baseline must be a non-empty list")

    test_cases = load_test_dataset()

    expected_ids = {
        case["test_id"] for case in test_cases
    }

    baseline_ids = set()

    for entry in baseline:
        required_fields = [
            "test_id",
            "prompt",
            "baseline_response"
        ]

        for field in required_fields:
            if field not in entry:
                raise ValueError(
                    f"Missing baseline field: {field}"
                )

        test_id = entry["test_id"]

        if test_id in baseline_ids:
            raise ValueError(
                f"Duplicate baseline test ID: {test_id}"
            )

        baseline_ids.add(test_id)

        if not isinstance(entry["baseline_response"], str) \
                or not entry["baseline_response"].strip():
            raise ValueError(
                f"Empty baseline response for {test_id}"
            )

    if baseline_ids != expected_ids:
        raise ValueError(
            "Baseline test IDs do not match the test dataset"
        )

    return baseline


if __name__ == "__main__":
    baseline = load_baseline()

    print("Baseline loaded successfully!")
    print("Total Baseline Responses:", len(baseline))

    for entry in baseline:
        print(
            entry["test_id"],
            "|",
            "Baseline available"
        )
