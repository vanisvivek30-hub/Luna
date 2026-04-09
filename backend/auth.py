import hashlib
from models import User, db

VALID_ROLES = {'student', 'org'}


def hash_password(password):
    """Hash password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()


def normalize_email(email):
    return (email or '').strip().lower()


def signup(email, password, name, role, college=None, domain=None, org_name=None, industry=None):
    """Register a new user."""
    try:
        email = normalize_email(email)
        role = (role or 'student').strip().lower()
        name = (name or '').strip()
        college = (college or '').strip() or None
        domain = (domain or '').strip() or None
        org_name = (org_name or '').strip() or None
        industry = (industry or '').strip() or None

        if not email or not password or not name:
            return {'success': False, 'message': 'Email, password, and name are required'}

        if len(password) < 8:
            return {'success': False, 'message': 'Password must be at least 8 characters'}

        if role not in VALID_ROLES:
            return {'success': False, 'message': 'Role must be student or org'}

        if role == 'student' and (not college or not domain):
            return {'success': False, 'message': 'Student signup requires college and domain'}

        if role == 'org' and (not org_name or not industry):
            return {'success': False, 'message': 'Organization signup requires org_name and industry'}

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {'success': False, 'message': 'Email already registered'}

        hashed_pw = hash_password(password)
        new_user = User(
            email=email,
            password=hashed_pw,
            name=name,
            role=role,
            college=college,
            domain=domain,
            org_name=org_name,
            industry=industry
        )
        db.session.add(new_user)
        db.session.commit()

        return {'success': True, 'message': 'User created successfully', 'user': new_user.to_dict()}
    except Exception as e:
        db.session.rollback()
        return {'success': False, 'message': f'Signup error: {str(e)}'}


def signin(email, password, role=None):
    """Authenticate user."""
    try:
        email = normalize_email(email)
        role = (role or '').strip().lower()

        user = User.query.filter_by(email=email).first()
        if not user:
            return {'success': False, 'message': 'User not found'}

        if role and role not in VALID_ROLES:
            return {'success': False, 'message': 'Invalid role supplied'}

        if role and user.role != role:
            return {'success': False, 'message': 'Role mismatch. Please sign in with the correct role.'}

        hashed_pw = hash_password(password)
        if user.password != hashed_pw:
            return {'success': False, 'message': 'Invalid password'}

        return {'success': True, 'message': 'Signed in successfully', 'user': user.to_dict()}
    except Exception as e:
        return {'success': False, 'message': f'Signin error: {str(e)}'}


def get_user(email):
    """Get user by email."""
    try:
        email = normalize_email(email)
        user = User.query.filter_by(email=email).first()
        return user.to_dict() if user else None
    except Exception as e:
        print(f'Error getting user: {str(e)}')
        return None


def get_all_users():
    """Get all users (for admin/org viewing)."""
    try:
        users = User.query.all()
        return [user.to_dict() for user in users]
    except Exception as e:
        print(f'Error getting users: {str(e)}')
        return []
