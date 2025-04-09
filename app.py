# 🔐 Secured Web Application

## Objective:
To create a secure web application where users can register, login, and logout safely using modern authentication methods.

## Technologies Used:
- Python (Flask Framework)
- MySQL (Database)
- bcrypt (For password encryption)
- HTML/CSS (Frontend Design)

## Key Features:
- **User Registration**: Users can sign up. Passwords are encrypted using `bcrypt`.
- **User Login**: Authenticates user credentials.
- **Session Management**: Maintains login state securely.
- **Logout**: Ends the session safely.

## How It Works:
1. **Register**: User submits form → Password is hashed and stored.
2. **Login**: Password is matched with hashed one in DB.
3. **Session**: If valid, session is created.
4. **Logout**: Session cleared, user logged out.

## Real-world Usage:
Can be used in admin dashboards, e-commerce logins, educational portals, etc.

## Simple Explanation for Viva:
> "Sir, yeh project Flask framework se bana hai. Isme user registration, login, aur logout functionality hai. Password securely bcrypt se encrypt kiya jata hai. Session handling se user ka login maintain hota hai."

## Screenshots:
### 🔐 Register Page
![Register Page](screenshot1.png)

### 🔑 Login Page
![Login Page](screenshot2.png)

## ✨ Developed By:
**Utkarsh Tripathi**
