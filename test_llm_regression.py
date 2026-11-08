
import pytest

from baseline_loader import load_baseline
from llm_client import generate_response
from similarity_checker import calculate_similarity


SIMILARITY_THRESHOLD = 0.75


@pytest.mark.parametrize("test_case", load_baseline())
def test_llm_regression(test_case):

    test_id = test_case["test_id"]
    prompt = test_case["prompt"]
    baseline_response = test_case["baseline_response"]

    actual_response = generate_response(prompt)

    similarity_score = calculate_similarity(
        baseline_response,
        actual_response
    )

    print(f"\nTest Case: {test_id}")
    print(f"Similarity Score: {similarity_score:.4f}")

    assert similarity_score >= SIMILARITY_THRESHOLD, (
        f"{test_id} regression failed! "
        f"Similarity: {similarity_score:.4f}, "
        f"Threshold: {SIMILARITY_THRESHOLD}"
    )
