from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play/<choice>")
def play(choice):

    choices = {
        "s": "Snake 🐍",
        "w": "Water 💧",
        "g": "Gun 🔫"
    }

    computer = random.choice(["s", "w", "g"])

    if choice == computer:
        result = "Draw 🤝"

    elif (
        (choice == "s" and computer == "w") or
        (choice == "g" and computer == "s") or
        (choice == "w" and computer == "g")
    ):
        result = "You Win 🎉"

    else:
        result = "Computer Wins 😢"

    return jsonify({
        "player": choices[choice],
        "computer": choices[computer],
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)