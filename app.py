
from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Function to analyze sentiment using TextBlob
def analyze_sentiment(review):
    blob = TextBlob(review)
    sentiment = blob.sentiment
    sentiment_label = 'Positive' if sentiment.polarity > 0 else 'Negative' if sentiment.polarity < 0 else 'Neutral'
    return {
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity,
        'sentiment': sentiment_label
    }
# Defining the home route that renders the index.html template
@app.route('/')
def home():
    return render_template('index.html')



# Defining the analyze route that handles POST requests for sentiment analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    review = data.get('review')
    
    if not review:
        return jsonify({"error": "No review text provided"}), 400
    
   # Analyzing the sentiment of the review text
    result = analyze_sentiment(review)
    
    return jsonify(result)

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
