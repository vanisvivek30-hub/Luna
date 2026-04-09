from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User
from auth import signup, signin, get_user, get_all_users
import os

app = Flask(__name__)

# ════════════ DATABASE CONFIGURATION ════════════
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}/industrysolve.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Create tables on startup
with app.app_context():
    db.create_all()
    print("✅ Database initialized at:", app.config['SQLALCHEMY_DATABASE_URI'])

# Enable CORS
CORS(app)

# ════════════ AUTHENTICATION ENDPOINTS ════════════

@app.route('/api/signup', methods=['POST'])
def api_signup():
    """User signup endpoint"""
    try:
        data = request.get_json()
        
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        name = data.get('name', '').strip()
        role = data.get('role', 'student').strip().lower()
        college = data.get('college', '').strip()
        domain = data.get('domain', '').strip()
        org_name = data.get('org_name', '').strip()
        industry = data.get('industry', '').strip()
        
        if not email or not password or not name:
            return jsonify({'success': False, 'message': 'Email, password, and name are required'}), 400
        
        if len(password) < 8:
            return jsonify({'success': False, 'message': 'Password must be at least 8 characters'}), 400
        
        result = signup(email, password, name, role, college, domain, org_name, industry)
        status = 201 if result['success'] else 400
        return jsonify(result), status
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/signin', methods=['POST'])
def api_signin():
    """User signin endpoint"""
    try:
        data = request.get_json()
        
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        role = data.get('role', '').strip().lower()
        
        if not email or not password:
            return jsonify({'success': False, 'message': 'Email and password are required'}), 400
        
        result = signin(email, password, role)
        status = 200 if result['success'] else 401
        return jsonify(result), status
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/user/<email>', methods=['GET'])
def api_get_user(email):
    """Get user profile"""
    try:
        user = get_user(email)
        if user:
            return jsonify({'success': True, 'user': user}), 200
        return jsonify({'success': False, 'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/users', methods=['GET'])
def api_get_all_users():
    """Get all users (admin endpoint)"""
    try:
        users = get_all_users()
        return jsonify({'success': True, 'users': users, 'total': len(users)}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# ════════════ HEALTH CHECK ════════════

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'Backend is running', 'database': 'SQLite', 'timestamp': str(__import__('datetime').datetime.now())}), 200

# ════════════ ERROR HANDLERS ════════════

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'message': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'success': False, 'message': 'Internal server error'}), 500

if __name__ == '__main__':
    print("🚀 Backend running on http://localhost:5000")
    print("📍 CORS enabled - Frontend can connect from any origin")
    print("💾 Database: SQLite (industrysolve.db)")
    app.run(debug=True, port=5000)
