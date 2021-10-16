from app import app
from flask import render_template, Blueprint, request
import os

#app = Blueprint('app', __name__)


@app.route("/")
def index():
    print(os.getcwd())
    return render_template("index.html")


@app.route("/about")
def about():
    return "All about Flask"


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return 'Logout'

@app.route("/qrcode")
def qrcode():
    print(os.getcwd())
    return render_template("qrcode.html")

@app.route('/form', methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        form = request.form
        print(form)
    return render_template('form.html')