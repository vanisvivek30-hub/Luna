# 🚀 BuildReal - Full Stack Setup Guide

## Backend Setup (Flask)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Backend Server
```bash
python app.py
```

The backend will start on **http://localhost:5000**

#### Available Endpoints:
- `POST /api/signup` - Register new user
- `POST /api/signin` - Login user  
- `GET /api/user/<email>` - Get user profile
- `GET /api/users` - Get all users (admin)
- `GET /api/health` - Health check

---

## Frontend Setup

### 1. Serve Frontend (choose one)

#### Option A: Using Python's built-in server
```bash
python -m http.server 8000
```
Then open **http://localhost:8000**

#### Option B: Using Live Server (VS Code Extension)
Install "Live Server" extension, then right-click on `index.html` → "Open with Live Server"

#### Option C: Using Node.js http-server
```bash
npm install -g http-server
http-server
```
Then open **http://localhost:8080**

---

## 🔗 How They Connect

1. **User signs up/in** on `signup.html` or `signin.html`
2. **Frontend calls** `http://localhost:5000/api/signup` or `/api/signin`  
3. **Backend validates** credentials and stores in database
4. **Response sent back** with user data
5. **Frontend stores** in `sessionStorage` for quick access
6. **User redirected** to `problem.html` dashboard
7. **problem.html loads** user data from `sessionStorage`

---

## 📝 Test Accounts

Once backend is running, you can:
- Create new accounts via Sign Up page
- Sign in with created accounts
- Data persists during the session (stored in Flask's memory)

---

## ⚠️ Important Notes

- **CORS is enabled** - Frontend on port 8000 can call backend on port 5000
- **Backend port**: 5000
- **Frontend port**: 8000 (or use Live Server's port)
- **Database**: In-memory (data resets when server restarts)
- For production, use **PostgreSQL** instead of in-memory storage

---

## 🚦 Start Both Servers

**Terminal 1 (Backend):**
```bash
cd luna2
python app.py
```

**Terminal 2 (Frontend):**
```bash
cd luna2
python -m http.server 8000
```

Then open **http://localhost:8000** in your browser!
