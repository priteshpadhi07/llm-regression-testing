
from sentence_transformers import SentenceTransformer
from sentence_transformers import util


MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def calculate_similarity(expected_response, actual_response):

    if not expected_response or not actual_response:
        raise ValueError("Responses cannot be empty")

    embeddings = model.encode(
        [expected_response, actual_response],
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        embeddings[0],
        embeddings[1]
    )

    return float(similarity.item())


if __name__ == "__main__":

    expected = (
        "Regression testing verifies that software changes "
        "have not introduced new defects."
    )

    actual = (
        "Regression testing checks whether recent code changes "
        "have caused new bugs."
    )

    score = calculate_similarity(expected, actual)

    print("Semantic Similarity Score:", round(score, 4))
