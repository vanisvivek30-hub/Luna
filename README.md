# IndustrySolve

A full-stack web application connecting students with organizations to solve real-world challenges.

## Project Structure

```
luna2/
├── frontend/              # Frontend HTML/CSS files
│   ├── css/              # Stylesheets
│   │   ├── style.css
│   │   └── problem.css
│   ├── index.html        # Landing page
│   ├── signin.html       # Login page
│   ├── signup.html       # Registration page
│   └── problem.html      # Dashboard
├── backend/              # Backend API & Database
│   ├── app.py           # Flask application
│   ├── auth.py          # Authentication logic
│   ├── models.py        # SQLAlchemy models
│   ├── manage_db.py     # Database management tool
│   ├── requirements.txt # Python dependencies
│   └── industrysolve.db # SQLite database
├── docs/                # Documentation
│   ├── API_DOCUMENTATION.md
│   ├── BACKEND_SETUP.md
│   ├── DATABASE_INFO.md
│   ├── QUICK_START.md
│   └── other docs...
├── start_frontend.bat   # Frontend server launcher
├── start_backend.bat    # Backend server launcher
├── .venv/              # Python virtual environment
└── README.md           # This file
```

## Quick Start

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
cd ..
```

### 2. Start Backend
```bash
start_backend.bat
# Backend runs on http://localhost:5000
```

### 3. Start Frontend (New terminal)
```bash
start_frontend.bat
# Frontend runs on http://localhost:8000
```

### 4. Open Application
Open browser to `http://localhost:8000`

## API Endpoints

- `POST /api/signup` - Register new user
- `POST /api/signin` - Login user
- `GET /api/health` - Check API status
- `GET /api/user/<email>` - Get user details
- `GET /api/users` - Get all users

## Features

- User authentication (Student & Organization roles)
- Role-based dashboard
- Problem browsing and applications
- User profile management
- SQLite database persistence

## Documentation

See [docs/](docs/) folder for detailed documentation:
- [QUICK_START.md](docs/QUICK_START.md) - Quick reference guide
- [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) - API details
- [BACKEND_SETUP.md](docs/BACKEND_SETUP.md) - Backend setup
- [DATABASE_INFO.md](docs/DATABASE_INFO.md) - Database schema

## Technologies

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Flask 2.3.3, Python 3
- **Database**: SQLite with SQLAlchemy ORM
- **API**: RESTful JSON API with CORS support

## Database

Database file: `backend/industrysolve.db`

To view/manage database:
```bash
cd backend
python manage_db.py
```

## Contact

For questions or issues, refer to documentation in the `docs/` folder.
