from flask import Flask, render_template, request, redirect, session
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

users = {}  # Dummy in-memory DB

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome {session['username']}! <br><a href='/logout'>Logout</a>"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        users[username] = hashed
        return redirect('/')
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')
    if username in users and bcrypt.checkpw(password, users[username]):
        session['username'] = username
        return redirect('/')
    return 'Invalid credentials'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
