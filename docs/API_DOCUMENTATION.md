# 🎯 BuildReal Backend-Frontend Connection Complete

## ✅ Current Status

- **🚀 Backend (Flask)**: Running on `http://localhost:5000`
- **🌐 Frontend (HTML)**: Running on `http://localhost:8000`
- **🔗 Connection**: Active and working

---

## 📱 Access the Application

Open your browser and go to:
```
http://localhost:8000
```

---

## 🔐 Authentication Flow

### Sign Up Flow:
1. User fills signup form with email, password, name, and role (student/org)
2. Click "Create Account"
3. Frontend validates form inputs
4. **Frontend sends POST request** to `http://localhost:5000/api/signup`
5. Backend validates and stores user
6. Backend returns user data
7. Frontend stores in `sessionStorage` 
8. User redirected to dashboard (`problem.html`)
9. Dashboard loads user info from session

### Sign In Flow:
1. User enters email and password
2. Selects role (student or org)
3. Click "Sign In"
4. Frontend validates inputs
5. **Frontend sends POST request** to `http://localhost:5000/api/signin`
6. Backend authenticates user
7. Backend returns user data
8. Frontend stores in `sessionStorage`
9. User redirected to dashboard with their role

---

## 📡 API Endpoints

### POST `/api/signup` - Register New User
**Request:**
```json
{
  "email": "student@example.com",
  "password": "securepass123",
  "name": "John Doe",
  "role": "student",
  "college": "IIT Bombay",
  "domain": "Full-Stack"
}
```

**Response (Success):**
```json
{
  "success": true,
  "message": "User created successfully",
  "user": {
    "email": "student@example.com",
    "name": "John Doe",
    "role": "student",
    "college": "IIT Bombay",
    "domain": "Full-Stack"
  }
}
```

---

### POST `/api/signin` - Login User
**Request:**
```json
{
  "email": "student@example.com",
  "password": "securepass123",
  "role": "student"
}
```

**Response (Success):**
```json
{
  "success": true,
  "message": "Signed in successfully",
  "user": {
    "email": "student@example.com",
    "name": "John Doe",
    "role": "student"
  }
}
```

---

### GET `/api/user/<email>` - Get User Profile
**Request:**
```
GET http://localhost:5000/api/user/student@example.com
```

**Response:**
```json
{
  "success": true,
  "user": {
    "email": "student@example.com",
    "name": "John Doe",
    "role": "student"
  }
}
```

---

### GET `/api/users` - Get All Users (Admin)
**Request:**
```
GET http://localhost:5000/api/users
```

**Response:**
```json
{
  "success": true,
  "users": [
    { "email": "student@example.com", "name": "John Doe", "role": "student" },
    { "email": "org@example.com", "name": "GreenTech Labs", "role": "org" }
  ]
}
```

---

### GET `/api/health` - Health Check
**Request:**
```
GET http://localhost:5000/api/health
```

**Response:**
```json
{
  "status": "Backend is running",
  "timestamp": "2026-04-09 10:30:45.123456"
}
```

---

## 🧪 Test the Connection

### Using Browser Console:
```javascript
// Test signup
fetch('http://localhost:5000/api/signup', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'test@example.com',
    password: 'password123',
    name: 'Test User',
    role: 'student'
  })
})
.then(res => res.json())
.then(data => console.log(data));

// Test signin
fetch('http://localhost:5000/api/signin', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'test@example.com',
    password: 'password123'
  })
})
.then(res => res.json())
.then(data => console.log(data));

// Test health check
fetch('http://localhost:5000/api/health')
.then(res => res.json())
.then(data => console.log(data));
```

---

## 📊 Data Storage

**Current Storage Method**: In-Memory (Python Dictionary)
- Data persists only while server is running
- Resets when backend restarts
- ✅ Good for development & testing

**For Production**, upgrade to:
- PostgreSQL
- MongoDB
- Firebase
- Any SQL/NoSQL database

---

## 🔧 Architecture

```
┌─────────────────────────────────┐
│   Frontend (HTML/JS/CSS)        │
│  (Port 8000)                     │
│                                  │
│  - index.html                    │
│  - signup.html                   │
│  - signin.html                   │
│  - problem.html                  │
└─────────────┬────────────────────┘
              │
              │ HTTP Requests (JSON)
              │ (CORS Enabled)
              │
┌─────────────▼────────────────────┐
│   Backend (Flask)                │
│  (Port 5000)                      │
│                                  │
│  - app.py                        │
│  - auth.py (signup/signin logic) │
│  - models.py (User model)        │
│  - In-memory database            │
└─────────────────────────────────┘
```

---

## 🚨 Troubleshooting

### "Connection refused" or "localhost:5000 not responding"?
- Make sure backend is running: `python app.py`
- Check port 5000 is available
- Run: `netstat -ano | findstr :5000`

### "CORS Error" when calling API?
- Ensure `flask-cors` is installed: `pip install flask-cors`
- Restart backend after installing

### "Email already registered" when signing up?
- Data persists in memory while server runs
- Restart backend to clear data: `python app.py`

### Frontend not loading?
- Make sure frontend server is running: `python -m http.server 8000`
- Open browser to: `http://localhost:8000`

---

## 📝 Next Steps

1. ✅ Test signup with multiple users
2. ✅ Test signin with correct/incorrect credentials
3. ✅ Verify user data in dashboard
4. 🔄 Add more features (problems, applications, submissions)
5. 🔄 Upgrade to real database (PostgreSQL)
6. 🔄 Add email verification
7. 🔄 Add JWT authentication tokens
8. 🔄 Deploy to cloud (Heroku, AWS, etc.)

---

## 🎉 All Set!

Your full-stack application is now running:
- Frontend: http://localhost:8000
- Backend API: http://localhost:5000

Create an account and explore the BuildReal dashboard! 🚀
