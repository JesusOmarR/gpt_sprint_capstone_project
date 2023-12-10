from flask import Flask, render_template, request
from flask_socketio import SocketIO
from brain_module import ChatGPT


app = Flask(__name__)
socketio = SocketIO(app)

# Replace 'YOUR_CHATGPT_API_KEY' with your actual API key
CHATGPT_API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

chat = ChatGPT()


def chatgpt_prompt(prompt):

    response = chat.request_openai(prompt)
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    body_input = request.form.get("part-select")
    intensity_input = request.form.get("intensity-select")
    place_input = request.form.get("place-select")
    prompt = "give me a " + body_input + " routine with a" + intensity_input + " intensity at " + place_input
    response = chatgpt_prompt(prompt)
    return render_template("index.html", messages=response)



if __name__ == "__main__":
    app.run(debug=True)
