from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from .models import User
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from . import db
import os
import smtplib
from email.mime.multipart import MIMEMultipart

#import cv2

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route("/")
def index():
    print(os.getcwd())
    return render_template("index.html")


@auth.route("/about")
def about():
    return "All about Flask"


@auth.route('/profile')
def profile():
    return render_template('profile.html')


@auth.route('/form')
def form():
    if request.method == "POST":
        form = request.form
        print(form)
    return render_template('form.html')


@auth.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['prescription']
        f.save(secure_filename(f.filename))
        filename = "./temp.png"
        print()
        EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

        contacts = ['YourAddress@gmail.com', 'test@example.com']

        EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

        contacts = ['YourAddress@gmail.com', 'test@example.com']

        msg = MIMEMultipart()
        msg['Subject'] = 'Deliver these!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'swaroopbhat510@gmail.com'

        # cwd = os.getcwd()  # Get the current working directory (cwd)
        # files = os.listdir(cwd)  # Get all the files in that directory
        # print("Files in %r: %s" % (cwd, files))

        ImgFileName = './app/temp1.png'
        with open(ImgFileName, 'rb') as f:
            img_data = f.read()

        # Or use MIMEImage, etc
        text = MIMEText("test")
        msg.attach(text)
        att = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        # Don't forget to convert the message to multipart first!
        msg.attach(att)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


@auth.route('/qrcode', methods=["GET", "POST"])
def qrcode():
    if request.method == "POST":
        f = request.files['file']
        print(f)
        f.save(secure_filename(f.filename))
        # img = cv2.imread(f)
        # detector = cv2.QRCodeDetector()
        print("worked")
    return render_template('QR.html')


@auth.route('/medical', methods=["GET", "POST"])
def medical():
    print("asd")
    return render_template('medicalshop.html')
