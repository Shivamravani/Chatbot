from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Manually inserted responses for the chatbot
responses = {
    "hi": "Greetings, mortal!",
    "how are you": "Ha! I am every mighty! The storms rage, my hammer sings and my foes tremble. And how about you",
    "who are you": "I am Thor, God of Thunder, Son of Odin!",
    "who is jaduu": "Ahaa! God of Thunder thinks She is a DAFAR.",
    "where are you from": "I hail from Asgard, a realm of golden halls, mighty warriors and endless feasts!",
    
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").lower()
    bot_response = responses.get(user_message, "I don’t have a response for that.")
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
