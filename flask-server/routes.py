from flask import Flask
app = Flask(__name__)

@app.route("/add", methods=["POST"], strict_slashes=False)
def add_articles():
    console.log("add was called!")

    return {}