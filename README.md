# secured-web-app
A simple secure login system using Flask, React, and MySQL
# Secured Web Application 🔐

A secure login system using **Python Flask**, **React.js**, and **MySQL** with password hashing and basic protection against common attacks like SQL Injection and XSS.

## 🔧 Technologies Used
- Backend: Python (Flask), bcrypt, MySQL
- Frontend: React.js, Axios
- Tools: Git, GitHub

## 🚀 How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py

# Project: Secured Web Application

# Directory Structure:
# secured-web-app/
# ├── app.py
# ├── templates/
# │   ├── index.html
# │   ├── login.html
# │   └── register.html
# ├── static/
# │   └── style.css
# └── requirements.txt

# Below is the main backend file (app.py)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Add your MySQL root password if set
app.config['MYSQL_DB'] = 'secureapp'

mysql = MySQL(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and bcrypt.checkpw(password, user[2].encode('utf-8')):
            session['username'] = user[1]
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
