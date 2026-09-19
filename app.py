from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

chatbot_responses = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "سلام", "ہیلو"],
        "responses": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "وعلیکم السلام! میں آپ کی کیا مدد کر سکتا ہوں؟"]
    },
    "python": {
        "patterns": ["what is python", "python kya hai", "پائথন کیا ہے"],
        "responses": ["Python is a high-level, interpreted programming language known for its simplicity and readability."]
    },
    "owner": {
        "patterns": ["who made you", "creator", "chishti bro", "معین الدین"],
        "responses": ["I was developed by Moinuddin, Founder of Chishti Bro Computers and Developers."]
    },
    "help": {
        "patterns": ["help", "support", "مدد"],
        "responses": ["I am an NLP chatbot assistant built by Chishti Bro Computers and Developers. How can I assist you?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "خدا حافظ", "اللہ حافظ"],
        "responses": ["Goodbye! Have a great day ahead!", "Khuda Hafiz! Take care."]
    }
}

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    for intent, data in chatbot_responses.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return random.choice(data["responses"])
    return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.form.get("msg")
    response = get_bot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
    
