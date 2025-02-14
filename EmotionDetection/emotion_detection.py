import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=header)

    # Handle exceptions where text input is empty
    if response.status_code == 400:
        return {
        'anger'   : None,
        'disgust' : None,
        'fear'    : None,
        'joy'     : None,
        'sadness' : None,
        'dominant_emotion' : None
        }

    # Parse the response from the API
    response_json = json.loads(response.text)

    # Extract emotions and their scores
    emotions_data = response_json['emotionPredictions'][0]['emotion']
    
    # Find highest scoring emotion
    dominant_emotion = max(emotions_data, key=lambda item: item[1])
    emotions_data['dominant_emotion'] = dominant_emotion

    # Convert to dictionary and return
    return dict(emotions_data)

