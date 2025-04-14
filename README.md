# 🔐 Secured Web Application

A secure full-stack web application with robust authentication and protection against common web vulnerabilities like SQL Injection and XSS. Designed to demonstrate cybersecurity best practices in real-world applications.

## 🚀 Tech Stack

- **Frontend:** React.js
- **Backend:** Python (Flask/Django)
- **Database:** MySQL
- **Security:** bcrypt, parameterized queries, input sanitization

---

## 🔒 Security Features Implemented

| Feature | Description |
|--------|-------------|
| **Password Hashing** | Uses `bcrypt` to hash user passwords securely |
| **SQL Injection Protection** | Parameterized queries prevent injection attacks |
| **XSS Mitigation** | React auto-sanitizes output + manual validation |
| **CSRF Protection** | Tokens or header-based protection (optional) |
| **Session Management** | Secure session handling and login timeouts |
| **Access Control** | Role-based access and page-level restrictions |

---

## 📸 Screenshots

> Include 2–3 images of your login form, dashboard, and error handling screens here for visual impact.

---

## 💡 Why This Project?

This project was built to:
- Practice secure coding principles based on OWASP Top 10
- Simulate a real-world login system that prevents user data leakage
- Demonstrate capability in both frontend and backend technologies

---

## 📈 Impact

- Hardened against common attack vectors
- Code structured using MVC principles for scalability
- Great showcase of cybersecurity awareness for interviews

---

## 📦 How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/secured-web-application.git
cd secured-web-application

# Set up Python backend
cd backend
pip install -r requirements.txt
python app.py

# Set up React frontend
cd ../frontend
npm install
npm start
