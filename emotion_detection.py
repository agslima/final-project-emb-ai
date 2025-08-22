# final_project/emotion_detection.py

import requests
import json

def emotion_detector(text_to_analyze):
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
    
    # Parse response JSON
    response_json = response.json()
    
    # Return the `text` attribute of the response object
    return response_json.get("text", None)
