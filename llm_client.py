
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def generate_response(prompt):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        return result["response"].strip()

    except requests.exceptions.RequestException as error:
        raise RuntimeError(
            f"LLM API request failed: {error}"
        ) from error


if __name__ == "__main__":

    prompt = "What is regression testing?"

    answer = generate_response(prompt)

    print("Prompt:", prompt)
    print("LLM Response:", answer)
