from flask import Flask, render_template_string, request, jsonify
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

# ایچ ٹی ایم ایل اور سی ایس اسی کو یہیں اندر شامل کر دیا گیا ہے تاکہ کسی فولڈر کی ضرورت نہ پڑے
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Assistant with NLP - Chishti Bro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { font-family: Arial, sans-serif; }
        .chat-box { height: 380px; overflow-y: scroll; background-color: #f9f9f9; }
    </style>
</head>
<body class="d-flex flex-column min-vh-100 bg-light">
    <div class="container py-4 flex-grow-1">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card shadow">
                    <div class="card-header bg-success text-white">
                        <h5 class="mb-0">🤖 PythonBot (NLP Assistant)</h5>
                    </div>
                    <div class="card-body chat-box" id="chatbox">
                        <div class="text-muted text-center small mb-3">Chat session started...</div>
                        <div class="mb-2">
                            <span class="badge bg-secondary">Bot</span>
                            <div class="p-2 bg-light rounded d-inline-block">Hello! How can I help you today?</div>
                        </div>
                    </div>
                    <div class="card-footer">
                        <form id="chat-form" class="input-group">
                            <input type="text" id="messageInput" class="form-control" placeholder="Type your query..." required autocomplete="off">
                            <button class="btn btn-success" type="submit">Send</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer class="text-center py-3 bg-dark text-white mt-auto">
        <p class="mb-0 small">Created by <strong>Moinuddin</strong> | Founder of <strong>Chishti Bro Computers and Developers</strong></p>
    </footer>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {$("#chat-form").on("submit", function(event) {
                event.preventDefault();
                const rawText = $("#messageInput").val();
                
                const userHtml = `<div class="mb-2 text-end">
                                    <span class="badge bg-primary">You</span>
                                    <div class="p-2 bg-primary text-white rounded d-inline-block text-start">${rawText}</div>
                                  </div>`;
                $("#messageInput").val("");
                $("#chatbox").append(userHtml);
                $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);

                $.ajax({
                    data: { msg: rawText },
                    type: "POST",
                    url: "/get",
                }).done(function(data) {
                    const botHtml = `<div class="mb-2">
                                        <span class="badge bg-secondary">Bot</span>
                                        <div class="p-2 bg-light rounded d-inline-block">${data.response}</div>
                                     </div>`;
                    $("#chatbox").append(botHtml);
                    $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
                });
            });
        });
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.form.get("msg")
    response = get_bot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
