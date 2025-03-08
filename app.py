from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Manually inserted responses for the chatbot
responses = {
    "hi": "Greetings, mortal!",
    "how are you": "Ha! I am every mighty! The storms rage, my hammer sings and my foes tremble. And how about you",
    "who are you": "I am Thor, God of Thunder, Son of Odin!",
    "what is your weapon": "Mjolnir, forged in the heart of a dying star! None but the worthy may wield it.",
    "what is asgard": "Asgard is the realm eternal, home of the gods, where honor and glory reign supreme!",
    "who is your father": "Odin Allfather, the wise and powerful ruler of Asgard!",
    "who is your brother": "Loki, the trickster! A thorn in my side, yet still my kin.",
    "who is your best friend": "Many warriors stand by my side, but the Warriors Three and Lady Sif are among my closest allies!",
    "who is your enemy": "Many have dared challenge me—Frost Giants, Hela, even the Mad Titan Thanos! Yet none have truly bested me!",
    "what is your favorite drink": "Ah, the sweet nectar of Asgardian mead! No mortal brew can compare!",
    "do you like midgard": "Indeed! Midgard is filled with brave warriors, noble hearts, and the occasional mischief!",
    "what do you think of iron man": "Stark? A man of genius, yet with an ego rivaling that of a god!",
    "what do you think of captain america": "A true warrior! Honorable, brave, and worthy of lifting Mjolnir!",
    "can you fly": "With Mjolnir in hand, I soar through the heavens like lightning itself!",
    "what is your greatest battle": "I have fought many battles, but Ragnarok, the fall of Asgard, was among the fiercest!",
    "what is your purpose": "To protect the realms, smite evildoers, and feast in victory!",
    "what is your favorite color": "The deep blue of the stormy skies, and the silver gleam of Mjolnir!",
    "can you control lightning": "Aye! The storm bends to my will, striking down my foes with divine fury!",
    "what happens if someone unworthy lifts mjolnir": "They shall find it unmoving, for only the worthy may wield its power!",
    "what do you think of loki": "Loki is a deceiver, yet he is my brother. My heart wars between love and mistrust.",
    "are you a god": "Indeed! I am Thor, God of Thunder!",
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
