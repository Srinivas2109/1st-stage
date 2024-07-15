from flask import Flask, request, jsonify
from model import generate_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input")
    if not user_input:
        return jsonify({"error": "No user input provided"}), 400

    response_text = generate_response(user_input)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
