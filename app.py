from flask import Flask, render_template, request, jsonify
import os
from chatbot_logic import get_response, load_intents
import nltk

# Ensure NLTK data is downloaded before the server starts
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/wordnet')
except LookupError:
    print("Downloading NLTK dependencies...")
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('punkt_tab')

app = Flask(__name__)

# Construct absolute path to the data
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
DATA_PATH = os.path.join(BASE_DIR, "dataset", "qa_pairs.json")

# Load intents globally initially, but we will also reload in the route
intents = load_intents(DATA_PATH)

@app.route("/")
def index():
    """Route to render the main chat interface."""
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    """API endpoint to handle incoming chat messages and return responses."""
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400
        
    user_message = data['message']
    
    # Reload intents dynamically on each request so JSON updates apply instantly
    current_intents = load_intents(DATA_PATH)
    
    # Get the response using our NLP logic
    bot_response = get_response(user_message, current_intents)
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True, port=5000)
