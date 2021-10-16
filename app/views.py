from app import app
from flask import render_template, request
import os


@app.route("/")
def index():
    print(os.getcwd())
    return render_template("index.html")


