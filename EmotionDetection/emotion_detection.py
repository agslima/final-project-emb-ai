# final_project/emotion_detection.py

import requests
import json

def emotion_detector(text_to_analyze):

    # If input is blank, return None for all values
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # API endpoint for Watson NLP Emotion Detection
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Required header to specify the model
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON body
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request
    response = requests.post(url, headers=headers, json=input_json)

    # If server returns 400 (bad request), return None values
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }      

    # Convert response text to dictionary
    response_dict = response.json()  # json.loads(response.text) could also be used
    
    # Extract the first set of emotion scores
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Construct the output dictionary
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return result