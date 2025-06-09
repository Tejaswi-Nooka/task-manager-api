# 🧠 Task Manager API

A simple yet secure backend API to manage tasks, built with **FastAPI**, **JWT authentication**, and **SQLite**.  
Includes user registration/login and full CRUD functionality for managing personal tasks.

---

## 🚀 Tech Stack

- ⚡ FastAPI – async web framework
- 🔐 JWT Auth – secure user sessions
- 🗃️ SQLite + SQLAlchemy – lightweight database
- 🧾 Pydantic – data validation

---

## 📦 Installation

```bash
git clone https://github.com/Tejaswi-Nooka/task-manager-api.git
cd task-manager-api

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
````

Open: [http://localhost:8000/docs](http://localhost:8000/docs) – Swagger UI

---

## 🔐 Authentication Flow

1. Register a new user – `POST /register`
2. Login – `POST /login` (get JWT token)
3. Click **"Authorize" 🔒** in Swagger docs and paste:

   ```
   Bearer <your_token_here>
   ```

---

## ✅ Features

* Secure JWT-based authentication
* Isolated task data per user
* Swagger UI for easy API testing
* Modular file structure for easy extension

---

## 🧪 JWT Usage

Include your token in the header:

```http
Authorization: Bearer <your_token>
```

---

## 🙋 About Me

Created by **Tejaswi Nooka**
[GitHub](https://github.com/Tejaswi-Nooka) | [LinkedIn](https://www.linkedin.com/in/tejaswin99/)

---

## 📄 License

MIT – Use freely for personal or professional projects.


