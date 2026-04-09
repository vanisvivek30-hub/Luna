# ✅ Database Connected - BuildReal

## 📊 Database Status

| Component | Status | Details |
|-----------|--------|---------|
| **Database Type** | ✅ SQLite | File-based, zero-config |
| **Database File** | ✅ buildreal.db | Located in project folder |
| **Database Location** | ✅ `c:\Users\Vivek\Documents\luna2\buildreal.db` | Persistent storage |
| **ORM** | ✅ SQLAlchemy | Python ORM for database |
| **Backend** | ✅ Flask + SQLAlchemy | API + Database layer |
| **Frontend** | ✅ HTML/JS | Connected via HTTP |

---

## 🚀 Connection Details

### Database Configuration
```python
Database URI: sqlite:///buildreal.db
Type: SQLite
Location: Project root
Auto-created: Yes (on first run)
```

### User Table Schema
```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  email VARCHAR(120) UNIQUE NOT NULL,
  password VARCHAR(256) NOT NULL,
  name VARCHAR(120) NOT NULL,
  role VARCHAR(20) NOT NULL,  -- 'student' or 'org'
  college VARCHAR(120),
  domain VARCHAR(120),
  org_name VARCHAR(120),
  industry VARCHAR(120),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

---

## 📱 Working Flow

```
Frontend (HTML/JS)
      ↓
   HTTP Request (JSON)
      ↓
Flask Backend API
      ↓
SQLAlchemy ORM
      ↓
SQLite Database (buildreal.db)
      ↓
Persistent Storage ✅
```

---

## 🔐 Data Flow: Sign Up

1. User fills signup form
2. Frontend validates input
3. POST request → `http://localhost:5000/api/signup`
4. Backend receives request
5. **SQLAlchemy validates** email uniqueness
6. **Hash password** (SHA256)
7. **Create User object**
8. **Save to SQLite database** (persist)
9. Response sent back with user data
10. Frontend stores in sessionStorage
11. User redirected to dashboard

---

## 🔑 Data Flow: Sign In

1. User enters email & password
2. Frontend validates input
3. POST request → `http://localhost:5000/api/signin`
4. Backend receives request
5. **SQLAlchemy queries** database by email
6. **Compare hashed** passwords
7. **Return user data** from database
8. Frontend stores in sessionStorage
9. User redirected to dashboard

---

## 💾 Data Persistence

✅ **User data persists** across:
- Browser closes and reopens
- Backend restarts
- Frontend redirect
- All sessions

❌ **Data is NOT lost** when:
- Closing browser (unlike in-memory)
- Restarting backend (unlike in-memory)
- Application crashes

---

## 🔍 View Database

### Option 1: Using Management Tool
```bash
python manage_db.py
```

### Option 2: Using SQLite Browser
```bash
# Install SQLite viewer (optional)
pip install sqlitebrowser

# Or use online viewer at: https://sqlitebrowser.org/
```

### Option 3: Using Command Line
```bash
sqlite3 buildreal.db
sqlite> SELECT * FROM users;
sqlite> .quit
```

---

## 🧪 Test the Database Connection

### Using Browser Console

```javascript
// Sign up new user
fetch('http://localhost:5000/api/signup', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'student@college.com',
    password: 'password123',
    name: 'Rahul Sharma',
    role: 'student',
    college: 'IIT Delhi',
    domain: 'Full-Stack'
  })
})
.then(r => r.json())
.then(console.log);
```

**Expected Response:**
```json
{
  "success": true,
  "message": "User created successfully",
  "user": {
    "id": 1,
    "email": "student@college.com",
    "name": "Rahul Sharma",
    "role": "student",
    "college": "IIT Delhi",
    "domain": "Full-Stack",
    "created_at": "2026-04-09T10:30:45.123456",
    "updated_at": "2026-04-09T10:30:45.123456"
  }
}
```

---

## 📈 Benefits of SQLite

✅ **No Server Setup** - Works out of the box
✅ **Persistent Storage** - Data survives restarts
✅ **ACID Compliant** - Reliable transactions
✅ **Easy Backup** - Just copy buildreal.db
✅ **Great for Development** - Perfect for testing
✅ **Scalable** - Can handle 100,000+ users
⚠️ **Limited Concurrency** - Use PostgreSQL for production

---

## 🔄 File Structure

```
luna2/
├── app.py              ← Flask app with database config
├── models.py           ← User model (SQLAlchemy)
├── auth.py             ← Signup/signin logic
├── buildreal.db        ← SQLite database file ✨
├── requirements.txt    ← Dependencies (includes flask-sqlalchemy)
├── manage_db.py        ← Database management tool
├── signin.html         ← Frontend (calls API)
├── signup.html         ← Frontend (calls API)
└── problem.html        ← Dashboard (reads sessionStorage)
```

---

## ⚙️ Backend Architecture

```
┌─────────────────────────────────┐
│   Flask App (app.py)             │
│                                  │
│   - Route handlers               │
│   - Request validation           │
│   - Error handling               │
└─────────────┬────────────────────┘
              │
┌─────────────▼────────────────────┐
│   SQLAlchemy ORM (models.py)      │
│                                  │
│   - User model definition         │
│   - Table schema                 │
│   - Data validation              │
└─────────────┬────────────────────┘
              │
┌─────────────▼────────────────────┐
│   SQLite Database (buildreal.db)  │
│                                  │
│   - users table                  │
│   - Persistent storage           │
│   - ACID transactions            │
└─────────────────────────────────┘
```

---

## 🐛 Troubleshooting

### "Database locked" error
- Usually means backend crashed while writing
- Solution: Restart backend: `python app.py`

### "No such table: users"
- Database wasn't initialized properly
- Solution: Delete buildreal.db and restart backend

### Data not persisting
- Check if backend is actually saving to DB
- Run: `python manage_db.py` to view users

### Wrong database path
- Edit `app.py` line 11 to change database location
- Currently: `buildreal.db` in project root

---

## 📝 Next Steps

1. ✅ Test signup with real data
2. ✅ Test signin with created account
3. ✅ Check database with `manage_db.py`
4. 🔄 Add password reset functionality
5. 🔄 Add user profile update
6. 🔄 Add email verification
7. 🔄 Upgrade to PostgreSQL for production

---

## 🎉 You're All Set!

Your BuildReal application now has:
- ✅ Frontend (HTML/JS/CSS)
- ✅ Backend API (Flask)
- ✅ Database (SQLite)
- ✅ Authentication (Signup/Signin)
- ✅ Persistent Storage

**Start building! 🚀**
