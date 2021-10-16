from app import app
from flask import render_template
import os

@app.route("/")
def index():
    print(os.getcwd())
    return render_template("index.html")

@app.route("/about")
def about():
    return "All about Flask"