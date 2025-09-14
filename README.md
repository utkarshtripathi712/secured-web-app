# 🔐 Secured Web Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A demonstration of a web application built with a strong focus on security best practices. This project includes a secure user authentication system and is hardened against common web vulnerabilities like SQL Injection and Cross-Site Scripting (XSS).

## Features
- **Secure User Registration & Login:** A complete authentication flow.
- **Password Hashing:** Uses crypt to securely hash and salt user passwords, never storing them in plain text.
- **Input Validation:** All user inputs are validated on the server-side to prevent malicious data entry.

## Security Measures Implemented
This project was built to specifically defend against the following common attacks:

* **SQL Injection (SQLi):**
    * **Defense:** All database queries are executed using **prepared statements** (parameterized queries). This ensures that user input is treated as data, not as executable SQL code.

* **Cross-Site Scripting (XSS):**
    * **Defense:** All user-supplied content rendered on a page is properly **escaped and sanitized**. This prevents malicious scripts from being executed in the browsers of other users.

* **Insecure Password Storage:**
    * **Defense:** Passwords are never stored directly. They are hashed using the robust crypt algorithm, which includes a salt to protect against rainbow table attacks.

## Tech Stack
- **Backend:** Python (Flask/Django)
- **Frontend:** React.js
- **Database:** SQL (PostgreSQL/SQLite)
- **Security Libraries:** bcrypt

## Installation & Usage
1.  **Clone the Repository**
    git clone https://github.com/utkarshtripathi712/secured-web-app.git
    cd secured-web-app
2.  **Install Dependencies**
    pip install -r requirements.txt
3.  **Run the Application**
    python app.py

## License
Distributed under the MIT License.
