from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

openai.api_key = "your-api-key-here"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
