<p align="center">
    <h1 align="center">Hale & Healthy</h1>
</p>
<p align="center">
    <em><code>Your Personal Health Assistant</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/smruthig/Hale-and-Healthy?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/smruthig/Hale-and-Healthy?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/smruthig/Hale-and-Healthy?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/CSS3-09A5B.svg?style=flat&logo=CSS3&logoColor=white" alt="CSS3">
</p>
<hr>

##  Quick Links

> - [ Overview](#overview)
> - [ Features](#features)
> - [ Repository Structure](#repository-structure)
> - [ Getting Started](#getting-started)
>   - [ Installation](#installation)
>   - [Running Hale-and-Healthy](#running-hale-and-healthy)

---

##  Overview

Hale and Healthy is a healthcare web application designed to give users more control over and insight into their health. It provides various features to track health metrics, locate nearby pharmacies, securely share medical history, and more.

The application was built with a focus on user privacy and security. Medical data is encrypted and can only be accessed via QR codes that users generate themselves. Location services are also opt-in only.


---

##  Features

### Medical History Sharing

- Securely share your medical history with new healthcare providers by generating a unique QR code
- Scanning the code provides one-time access to your data

### Pharmacy Finder

- Enable location services to see real-time suggestions for nearby pharmacies to easily fill your prescriptions

### Exercise Recommendations

- Select a health target like losing weight or reducing stress and receive personalized home exercise recommendations

### Menstrual Tracking

- Use the built-in calendar and tools to track your cycle
- Set reminders for periods, symptoms, self-care activities, and more

### Medicine Reminders

- Input your medications and dosing schedule to receive reminder notifications for when to take your next dose

### Food Logging

- Use the food database to log meals and snacks
- View nutrition statistics over time

### Progress Dashboards:

- Visualize your activity completion rates, weight trends, cycle tracking, and more on the easy-to-read personal dashboards

---

##  Repository Structure

```sh
└── Hale-and-Healthy/
    ├── AllDetails.csv
    ├── README.md
    ├── Todo.md
    ├── __pycache__
    │   └── main.cpython-39.pyc
    ├── app
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── auth.cpython-37.pyc
    │   │   ├── auth.cpython-39.pyc
    │   │   ├── main.cpython-37.pyc
    │   │   ├── main.cpython-39.pyc
    │   │   ├── models.cpython-37.pyc
    │   │   ├── models.cpython-39.pyc
    │   │   └── views.cpython-39.pyc
    │   ├── auth.py
    │   ├── db.sqlite3
    │   ├── main.py
    │   ├── models.py
    │   ├── static
    │   │   ├── assets
    │   │   │   ├── favicon.ico
    │   │   │   ├── hhlogo.jfif
    │   │   │   ├── homescreenmainimage.png
    │   │   │   └── img
    │   │   │       ├── about
    │   │   │       ├── close-icon.svg
    │   │   │       ├── header-bg.jpg
    │   │   │       ├── hhlogo.jpg
    │   │   │       ├── logos
    │   │   │       ├── map-image.png
    │   │   │       ├── navbar-logo.svg
    │   │   │       ├── portfolio
    │   │   │       ├── team
    │   │   │       └── workout
    │   │   ├── css
    │   │   │   ├── bootstrap.css
    │   │   │   ├── style_reminder.css
    │   │   │   └── styles.css
    │   │   └── js
    │   │       ├── app.js
    │   │       ├── jquery-3.5.1.js
    │   │       └── scripts.js
    │   └── templates
    │       ├── QR.html
    │       ├── app.js
    │       ├── base.html
    │       ├── doctorappointment.html
    │       ├── fitness.html
    │       ├── form.html
    │       ├── index.html
    │       ├── login.html
    │       ├── medicalshop.html
    │       ├── menstrualtracker.html
    │       ├── profile.html
    │       ├── qrcode.html
    │       ├── reminder.html
    │       └── signup.html
    ├── doc.csv
    ├── notes.csv
    └── temp1.png
```

## Getting Started

###  Installation

1. Clone the Hale-and-Healthy repository:

```sh
git clone https://github.com/smruthig/Hale-and-Healthy
```

2. Change to the project directory:

```sh
cd Hale-and-Healthy
```

3. Install the dependencies:

```sh
npm install
```

###  Running `Hale-and-Healthy`

Use the following command to run Hale-and-Healthy:

```sh
npm start
```

