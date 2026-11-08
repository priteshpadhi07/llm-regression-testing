
import json
from pathlib import Path

from test_executor import execute_test_cases


BASELINE_FILE = Path(__file__).parent / "baseline_responses.json"


def save_baseline():
    results = execute_test_cases()

    failed_cases = [
        result for result in results
        if result["status"] != "EXECUTED"
        or not result["actual_response"].strip()
    ]

    if failed_cases:
        raise RuntimeError(
            "Cannot create baseline: some test cases failed execution"
        )

    baseline = []

    for result in results:
        baseline.append({
            "test_id": result["test_id"],
            "prompt": result["prompt"],
            "baseline_response": result["actual_response"]
        })

    with open(BASELINE_FILE, "w", encoding="utf-8") as file:
        json.dump(baseline, file, indent=4, ensure_ascii=False)

    print("\nBaseline saved successfully!")
    print("Total Baseline Responses:", len(baseline))
    print("File:", BASELINE_FILE.name)


if __name__ == "__main__":
    save_baseline()
