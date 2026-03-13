import json
import requests # Import the requests library to handle HTTP requests

def sentiment_analyzer(text_to_analyse):
    """Define a function named sentiment_analyzer that takes a 
    string input (text_to_analyse)"""
    # URL of the sentiment analysis service 
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' 
    # Create a dictionary with the text to be analyzed 
    myobj = { "raw_document": { "text": text_to_analyse } } 
    # Set the headers required for the API request 
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} 

    # Send a POST request to the API with the text and headers 
    response = requests.post(url, json = myobj, headers=header) 
    # Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        # Extracting sentiment label and score from the response 
        label = formatted_response.get('documentSentiment',{}).get('label', '') 
        sentiment = label.split('_')[-1]
        score = formatted_response.get('documentSentiment',{}).get('score', 0)
    elif response.status_code == 500:
        label = None 
        sentiment = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score, 'sentiment': sentiment}