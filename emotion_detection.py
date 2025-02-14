import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=header)

    # Parse the response from the API
    response_json = json.loads(response.text)

    # Extract emotions and their scores
    emotions_data = [
        ('anger'  , response_json['emotionPredictions'][0]['emotion']['anger']),
        ('disgust', response_json['emotionPredictions'][0]['emotion']['disgust']),
        ('fear'   , response_json['emotionPredictions'][0]['emotion']['fear']),
        ('joy'    , response_json['emotionPredictions'][0]['emotion']['joy']),
        ('sadness', response_json['emotionPredictions'][0]['emotion']['sadness']),
        ]
    
    # Find highest scoring emotion
    dominant_emotion = max(emotions_data, key=lambda item: item[1])
    emotions_data.append(('dominant_emotion', dominant_emotion[0]))

    # Convert to dictionary and return
    return dict(emotions_data)

