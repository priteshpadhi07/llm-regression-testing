
from llm_client import generate_response
from similarity_checker import calculate_similarity


CONSISTENCY_THRESHOLD = 0.85


def check_consistency(prompt, runs=3):

    responses = []

    for i in range(runs):
        print(f"Generating Response {i + 1}...")

        response = generate_response(prompt)
        responses.append(response)

    scores = []

    for i in range(len(responses)):
        for j in range(i + 1, len(responses)):

            score = calculate_similarity(
                responses[i],
                responses[j]
            )

            scores.append(score)

            print(
                f"Response {i + 1} vs Response {j + 1}:",
                round(score, 4)
            )

    minimum_score = min(scores)

    status = (
        "PASS"
        if minimum_score >= CONSISTENCY_THRESHOLD
        else "FAIL"
    )

    print("\nConsistency Test Summary")
    print("Total Responses:", len(responses))
    print("Minimum Similarity:", round(minimum_score, 4))
    print("Status:", status)


if __name__ == "__main__":

    prompt = "What is software regression testing?"

    check_consistency(prompt)
