import json
import requests # Import the requests library to handle HTTP requests


def get_dominant_emotion(emotions: dict[str, float]) -> str:
    if not emotions:
        raise ValueError("emotions dict is empty")
    return max(emotions, key=emotions.get)


def emotion_detector(text_to_analyse: str) -> dict:
    """Call Watson NLP Emotion API and return emotions plus dominant_emotion."""
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=payload, headers=headers)

    status_code = response.status_code

    if status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    if status_code != 200:
        return {}

    formatted_response = response.json()

    # emotionPredictions is a list; take the first element if present
    emotion_predictions = formatted_response.get("emotionPredictions", [])
    if not emotion_predictions:
        return {}

    predictions = emotion_predictions[0]
    emotions = predictions.get("emotion", {})
    if not emotions:
        return {}

    dominant = get_dominant_emotion(emotions)
    emotions["dominant_emotion"] = dominant
    return emotions