"""
Web server for emotion detection
localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

def format_emotion_response(emotions: dict) -> str:
    """Build HTML text from an emotions dict, with dominant emotion in bold."""
    if not emotions:
        return "No emotions could be detected for the given statement."

    dominant = emotions.get("dominant_emotion", "unknown")
    scores = {k: v for k, v in emotions.items() if k != "dominant_emotion"}

    parts = [f"'{name}': {value}" for name, value in scores.items()]
    scores_str = ", ".join(parts)

    return (
        f"For the given statement, the system response is {scores_str}. "
        f"The dominant emotion is <strong>{dominant}</strong>."
    )

@app.route("/emotionDetector")
def em_detector():
    """ 
    Retrieve the text to analyze from the request arguments 
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze) or {}
    return format_emotion_response(response)


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
