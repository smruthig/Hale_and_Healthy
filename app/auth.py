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
from csv import writer, reader
import cv2
import random
import base64
import pandas as pd

auth = Blueprint('auth', __name__)
glo = []
ema = ''
na = ''


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    try:
        if not user and not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
    except Exception:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    global na
    na = user.name
    login_user(user, remember=remember)
    with open('notes.csv', newline='') as f:
        reade = reader(f)
        data = list(reade)
        print(data)
    for i in data:
        if i[0] == email:
            global glo
            glo = i
            break
    global ema
    ema = email
    print(glo)

    return render_template("index.html", xyz=glo)


@auth.route('/signup')
def signup():
    return render_template('signup.html')


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


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
    List = []
    List.append(email)
    List.append(name)
    List.append(' ')
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('notes.csv', 'a') as f_object:

        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()

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
def uploader():
    if request.method == 'POST':
        f = request.files['prescription']
        f.save("/tmp/temp1.png")

        EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

        msg = MIMEMultipart()
        msg['Subject'] = 'Deliver these!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'swaroopbhat510@gmail.com'

        # cwd = os.getcwd()  # Get the current working directory (cwd)
        # files = os.listdir(cwd)  # Get all the files in that directory
        # print("Files in %r: %s" % (cwd, files))

        ImgFileName = '/tmp/temp1.png'
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
        return 'file uploaded successfully'
    return render_template('medicalshop.html')


@auth.route('/qrcode', methods=["GET", "POST"])
def qrcode():
    if request.method == "POST":
        f = request.form["qr"]
        decodeit = open('/tmp/qr.jpeg', 'wb')
        decodeit.write(base64.b64decode(bytes(f+"====", encoding="utf-8")))
        decodeit.close()
        img = cv2.imread("/tmp/qr.jpeg")
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if bbox is not None:
            df = pd.read_csv('doc.csv')
            global ema
            print(ema)
            qdf = df[df['email'] == ema]
            print(qdf)
            s = qdf.to_dict()
            print(s)
            global na
            s1 = "The below is the medical info of "+na+". PFA the prescription.\n"
            for i, j in s.items():
                print(i)
                s1 += str(i)+": "+str(j[0])+'\n'
            msg = MIMEMultipart()
            text = MIMEText(s1)

            msg.attach(text)
            ImgFileName = '/tmp/temp1.png'
            with open(ImgFileName, 'rb') as f:
                img_data = f.read()
            att = MIMEImage(img_data, name=os.path.basename(ImgFileName))
            # Don't forget to convert the message to multipart first!
            msg.attach(att)
            EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
            EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
            msg['Subject'] = 'Client: '+na
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = 'swaroopbhat510@gmail.com'

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            return "<a href={}> <center> Click here for patient's details</a>".format(data)
        else:
            return render_template('QR.html')
    else:
        return render_template('QR.html')


@auth.route('/update', methods=["POST"])
def update():
    fl = request.form['notes']

    print(fl)
    with open('notes.csv', newline='') as f:
        reade = reader(f)
        data = list(reade)
        print(data)
        global ema
        j = 0
        for i in data:
            if i[0] == ema:
                global glo
                glo = i
                break
            j += 1
        print(glo)

        # reading the csv file
        df = pd.read_csv("notes.csv")
        print(j)
        # updating the column value/data
        df.loc[df['email'] == ema, 'notes'] = fl
        print(df)
        # writing into the file
        df.to_csv("notes.csv", index=False)
        return "working"


# @auth.route('/medical', methods=["GET", "POST"])
# def medical():
#     print("asd")
#     return render_template('medicalshop.html')

@auth.route('/foqw', methods=["GET", "POST"])
def mainform():
    if request.method == "POST":
        print(request.form)
        # id,name,doa,weight,height,age,symptoms(block),doctor,diagnosis(block),prescription(block)
        df = pd.read_csv('doc.csv')
        id = df.shape[0]
        l = list()
        l.append(id)
        l.append(na)
        res = l + list(request.form.values())
        res.pop(-1)
        f = request.files["prescription"]
        # print(f)
        f.save("/tmp/temp"+str(id)+".png")
        res.append("/tmp/temp"+str(id)+".png")
        # print(res)
        with open('doc.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(res)
            f_object.close()
        return render_template('form.html')
