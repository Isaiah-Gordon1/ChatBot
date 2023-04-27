import json
from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load knowledge base from JSON file
with open("knowledge.json", "r") as f:
    knowledge = json.load(f)["knowledge"]

# Define function to save new knowledge to JSON file
def save_knowledge():
    with open("knowledge.json", "w") as f:
        json.dump({"knowledge": knowledge}, f, indent=4)

# Define function to get response from knowledge base
def get_response(message):
    for item in knowledge:
        if message.lower() == item["user_input"].lower():
            return item["bot_response"]
    return None

@app.route('/teach', methods=['GET', 'POST'])
def teach():
    if request.method == 'POST':
        # Handle the form submission
        return redirect(url_for('home'))
    else:
        # Render the form
        return render_template('teach.html')

@app.route("/add_knowledge", methods=["POST"])
def add_knowledge():
    data = request.get_json()
    knowledge.append({
        "user_input": data["user_input"],
        "bot_response": data["bot_response"]
    })
    save_knowledge()
    return jsonify({"message": "Knowledge added successfully."})

# Flask app code
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/send_message", methods=["POST"])
def send_message():
    try:
        message = request.get_json()["message"]
    except KeyError:
        return jsonify({"message": "Invalid request format. Please provide a 'message' key in your request.", "prompt": True})
    response = get_response(message)
    if response is None:
        return jsonify({"message": "I don't know what you mean. Please provide a response.", "prompt": True})
    else:
        return jsonify({"message": response, "prompt": False})

if __name__ == "__main__":
    app.run(debug=True)
