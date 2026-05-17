from flask import Flask, request, render_template
import json
from EmotionDetection.EmotionDetection import emotion_detector

app = Flask("emotion_detector")

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Please provide text to analyze using the 'textToAnalyze' query parameter."

    formatted_response = emotion_detector(text_to_analyze)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    emotion_items = [f"'{k}': {v:.9f}" for k, v in emotions.items()]
    if len(emotion_items) > 1:
        emotions_str = ', '.join(emotion_items[:-1]) + ' and ' + emotion_items[-1]
    else:
        emotions_str = emotion_items[0]

    result_str = (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return result_str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)