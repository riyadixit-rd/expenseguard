# 🚀 ExpenseGuard – Expense Fraud Detection System

A full-stack web application that detects fraudulent expenses using rule-based logic, with role-based access for Admin and Users.

---

## 🔥 Features

- 🔐 Login System (Admin & User roles)
- 📊 Dashboard with real-time expense tracking
- ⚠️ Fraud Detection based on expense amount
- ➕ Add Expenses dynamically
- 👨‍💼 Admin Panel to manage entries
- 🌐 Fully deployed (Frontend + Backend)

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- FastAPI (Python)
- SQLite Database

### Deployment
- Frontend: Netlify
- Backend: Render

---

## 📂 Project Structure
expenseguard/
│
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── auth.py
│ └── frontend/
│ ├── index.html
│ ├── dashboard.html
│ ├── admin.html
│
├── expenses.db
├── requirements.txt
└── README.md

---

## ⚙️ How It Works

1. User logs in (Admin/User)
2. Admin can add employees (expenses)
3. Expenses are analyzed using fraud logic:
   - Amount > 50,000 → Fraud
   - Amount > 20,000 → Medium Risk
   - Otherwise → Safe
4. Dashboard displays:
   - Total Expenses
   - Fraud Count
   - Safe Transactions

---

## 🌐 Live Demo

- Frontend: [neon-genie-4296fd.netlify.app](https://neon-genie-4296fd.netlify.app/)
- Backend API: https://expenseguard-api.onrender.com  

---

## 📌 API Endpoints

- `POST /login` → User login  
- `GET /expenses` → Fetch all expenses  
- `POST /add_expense` → Add new expense  

---

## 🧠 Key Learnings

- Full-stack development (Frontend + Backend)
- REST API integration
- Debugging real-world deployment issues
- Working with databases (SQLite)
- Hosting apps using Netlify & Render

---

## 👨‍💻 Author

**Riya Dixit**
