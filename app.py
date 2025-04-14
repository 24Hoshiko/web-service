from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/message")
def message():
    return jsonify(message="Hello from Flask on Heroku with a pretty UI!")

if __name__ == "__main__":
    app.run()
