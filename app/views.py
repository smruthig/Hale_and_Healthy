from app import app
from flask import render_template, Blueprint
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
