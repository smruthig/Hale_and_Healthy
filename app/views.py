from app import app
from flask import render_template, request
import os


@app.route("/")
def index():
    print(os.getcwd())
    return render_template("index.html")


@app.route("/details", methods=["POST","GET"])
def details():
    if request.method == "POST":
        form = request.form
        print(form)
    return render_template("details.html")

@app.route("/qrcode")
def qrcode():
    print(os.getcwd())
    return render_template("qrcode.html")