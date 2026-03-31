import json
import random
import re
import nltk
from nltk.stem import WordNetLemmatizer

# In a real environment, you might need to run these once:
# nltk.download('punkt')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load the intents file
def load_intents(filepath):
    try:
        with open(filepath, 'r') as file:
            intents = json.load(file)
        return intents
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return {"intents": []}

# A larger custom set of stop words to ignore out common pronouns and verbs
STOP_WORDS = {
    "what", "is", "the", "are", "do", "does", "did", "you", "a", "an", "of", "to", "in", 
    "like", "about", "tell", "me", "i", "am", "want", "know", "can", "could", "for", "how", 
    "when", "where", "why", "who", "which", "my", "your", "this", "that", "it", "on", "at", 
    "by", "with", "from", "and", "or", "have", "has", "had", "will", "would", "shall", "should"
}

# Preprocess text (tokenize and lemmatize)
def clean_up_sentence(sentence):
    # Tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # Lemmatize each word -> lower case, and filter out stop words
    cleaned_words = [
        lemmatizer.lemmatize(word.lower()) 
        for word in sentence_words 
        if word.lower() not in STOP_WORDS and word.isalnum()
    ]
    return cleaned_words

# Simple bag of words scoring or keyword matching
def get_response(user_input, intents_json):
    user_input_cleaned = clean_up_sentence(user_input)
    
    # Store tag scores
    tag_scores = {}
    
    for intent in intents_json['intents']:
        tag = intent['tag']
        patterns = intent['patterns']
        
        # Calculate a score based on word overlap
        best_pattern_score = 0
        for pattern in patterns:
            pattern_words = clean_up_sentence(pattern)
            # Count common words
            common_words = set(user_input_cleaned).intersection(set(pattern_words))
            current_score = len(common_words)
            
            # Exact substring match gives a high score
            if pattern.lower() in user_input.lower():
                current_score += 5
                
            if current_score > best_pattern_score:
                best_pattern_score = current_score
                
        tag_scores[tag] = best_pattern_score
        
    # Find the tag with the highest score
    if tag_scores:
        best_tag = max(tag_scores, key=tag_scores.get)
        best_score = tag_scores[best_tag]
        
        # If the highest score is 0, we didn't understand
        if best_score == 0:
            return "I'm sorry, I don't quite understand. Could you rephrase your question? Try asking about courses, fees, timings, or hostel facilities."
            
        # Get a random response for the best tag
        for intent in intents_json['intents']:
            if intent['tag'] == best_tag:
                return random.choice(intent['responses'])
                
    return "I'm sorry, I'm having trouble retrieving the information right now."

if __name__ == "__main__":
    # Small test loop if run directly
    intents = load_intents('dataset/qa_pairs.json')
    print("Chatbot is ready! Type 'exit' to stop.")
    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        print("Bot:", get_response(msg, intents))
