from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    # call your translation logic here
    return jsonify({"translated": text})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
