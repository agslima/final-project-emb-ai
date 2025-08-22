# final_project/server.py

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Emotion detection route
@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    if request.method == 'POST':
        # Get JSON payload from POST request
        data = request.get_json()
        text_to_analyze = data.get('text', '')
    else:  # GET request
        # Get text from query parameter for quick testing
        text_to_analyze = request.args.get('textToAnalyze', '')

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # If dominant_emotion is None, display error message
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"})

# Run Flask server on localhost:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
