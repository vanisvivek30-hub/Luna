# ⚡ Quick Start Reference

## 🟢 Servers Running

| Service  | URL | Port | Status | Database |
|----------|-----|------|--------|----------|
| Frontend | http://localhost:8000 | 8000 | ✅ Running | — |
| Backend  | http://localhost:5000 | 5000 | ✅ Running | SQLite |
| Database | buildreal.db | — | ✅ Active | Persistent |

---

## 🎯 Quick Access

- **Open App**: http://localhost:8000
- **Sign Up**: http://localhost:8000/signup.html
- **Sign In**: http://localhost:8000/signin.html  
- **Dashboard**: http://localhost:8000/problem.html
- **API Docs**: See `API_DOCUMENTATION.md`
- **Database**: See `DATABASE_INFO.md`

---

## 💾 Database

**Type**: SQLite (File-based)  
**File**: `buildreal.db`  
**Location**: Project root  
**ORM**: SQLAlchemy  
**Persistence**: ✅ Yes - Data survives restarts

### View Database Users
```bash
python manage_db.py
```

Output shows all registered users with email, name, role, college/org, and signup date.

---

## 🔌 Connection Test

Paste in browser console to test API:
```javascript
fetch('http://localhost:5000/api/health').then(r=>r.json()).then(console.log)
```

Expected response:
```json
{"status": "Backend is running", "database": "SQLite", "timestamp": "..."}
```

---

## 📋 Key Files

| File | Purpose |
|------|---------|
| `app.py` | Flask backend + database config |
| `auth.py` | Signup/signin/database logic |
| `models.py` | SQLAlchemy User model |
| `buildreal.db` | SQLite database file |
| `manage_db.py` | View/manage database |
| `signin.html` | Login page (calls `/api/signin`) |
| `signup.html` | Registration page (calls `/api/signup`) |
| `problem.html` | Dashboard (reads from sessionStorage) |

---

## 🚀 Data Flow (with Database)

```
1. User fills signup/signin form
        ↓
2. Frontend validates input
        ↓
3. Frontend sends JSON to http://localhost:5000/api/signin
        ↓
4. Backend validates & checks SQLite database
        ↓
5. Backend responses with user data
        ↓
6. Frontend stores in sessionStorage
        ↓
7. Frontend redirects to problem.html
        ↓
8. Dashboard displays actual signed-in user
```

---

## 💾 Persistent Storage

Unlike before (in-memory):
- ✅ User data **persists** after backend restart
- ✅ User data **persists** across sessions
- ✅ User data **persists** when closing browser
- ✅ Data backed up in `buildreal.db` file

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask (Python) |
| **Database** | SQLite 3 |
| **ORM** | SQLAlchemy |
| **API** | RESTful JSON |
| **Auth** | SHA256 Password Hashing |

---

## 📊 Database Schema

**Users Table:**
- `id` - Primary key
- `email` - Unique, indexed
- `password` - Hashed SHA256
- `name` - Full name
- `role` - 'student' or 'org'
- `college` - For students
- `domain` - For students (Full-Stack, Backend, etc.)
- `org_name` - For organizations
- `industry` - For organizations
- `created_at` - Timestamp
- `updated_at` - Timestamp

---

## ⚠️ Stop Servers

**Windows:**
- Backend: Press `Ctrl+C` in backend terminal
- Frontend: Press `Ctrl+C` in frontend terminal

Database file (`buildreal.db`) will be preserved.

---

## 📞 Support Files

Check these for more info:
- `BACKEND_SETUP.md` - Full setup instructions
- `API_DOCUMENTATION.md` - Complete API reference
- `DATABASE_INFO.md` - Database details & queries
- `requirements.txt` - All dependencies

---

## ✨ You're Connected!

Frontend ←→ Backend ←→ Database ✅

Ready to use!
