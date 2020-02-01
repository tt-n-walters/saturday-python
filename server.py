from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    if request.args.get("position") and request.args.get("position") == "66665":
        return "Correct! Nicely done."
    else:
        return "hi"

app.run(host="0.0.0.0", port=8000)
