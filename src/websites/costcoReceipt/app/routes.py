from flask import render_template
from app import app


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html", title="Welcome")
