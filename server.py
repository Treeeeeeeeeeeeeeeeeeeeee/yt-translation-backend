from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

PORT = int(os.environ.get("PORT", 5000))

OPENAI_API_KEY = os.environ.get("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")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    target_lang = data.get("lang", "en")

    if not OPENAI_API_KEY:
        return jsonify({"error": "OpenAI key not configured"}), 500

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {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}"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": f"Translate to {target_lang}."},
            {"role": "user", "content": text}
        ]
    }

    r = requests.post(url, headers=headers, json=payload)
    resp = r.json()

    translated = resp["choices"][0]["message"]["content"]
    return jsonify({"translated": translated})

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=PORT)
