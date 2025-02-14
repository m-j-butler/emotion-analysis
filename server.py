'''Executing function initiates application of sentiment analysis, 
to be executed over Flask channel and deployed on localhost:5000.'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''Receives text from the HTML interface and runs
    emotion detection on it using the emotion_detector()
    function. Output returns a dictionary of emotions
    with their score.'''

    input_text = request.args.get('textToAnalyze')
    response = emotion_detector(input_text)

    output = f"For the given statement, the system response is\
    'anger': {response['anger']}, \
    'disgust': {response['disgust']}, \
    'fear': {response['fear']}, \
    'joy': {response['joy']} and \
    'sadness': {response['sadness']}.\
    The dominant emotion is {response['dominant_emotion']}."

    # Handling user input of empty text
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return output


@app.route("/")
def render_index_page():
    '''Initiates rendering of main application page
    over the Flask channel.'''

    return render_template('index.html')


if __name__ == '__main__':
    # Executes Flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
