from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User
from auth import signup, signin, get_user, get_all_users
import os
from datetime import datetime

app = Flask(__name__)

# ════════════ DATABASE CONFIGURATION ════════════
db_url = os.environ.get('DATABASE_URL')
# For SQLAlchemy 1.4+ compatibility (Render uses postgres:// by default)
if db_url and db_url.startswith('postgres://'):
    db_url = db_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url or 'postgresql://lunadb_klet_user:lpAqXidCpdgdTUQ2iEfrUKebvmNyilBu@dpg-d7ckbtn41pts73dha9q0-a.oregon-postgres.render.com/lunadb_klet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Enable CORS
CORS(app)

try:
    with app.app_context():
        db.create_all()
        print("✅ Database initialized successfully", flush=True)
except Exception as e:
    print(f"❌ Database initialization failed: {e}", flush=True)
    # Don't exit here, let the app try to start anyway or gunicorn==23.0.0 will catch the startup failure

# ════════════ AUTHENTICATION ENDPOINTS ════════════

@app.route('/api/signup', methods=['POST'])
def api_signup():
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
        return jsonify(result), (201 if result['success'] else 400)

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/signin', methods=['POST'])
def api_signin():
    try:
        data = request.get_json()

        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        role = data.get('role', '').strip().lower()

        if not email or not password:
            return jsonify({'success': False, 'message': 'Email and password are required'}), 400

        result = signin(email, password, role)
        return jsonify(result), (200 if result['success'] else 401)

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/user/<email>', methods=['GET'])
def api_get_user(email):
    try:
        user = get_user(email)
        if user:
            return jsonify({'success': True, 'user': user}), 200
        return jsonify({'success': False, 'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/users', methods=['GET'])
def api_get_all_users():
    try:
        users = get_all_users()
        return jsonify({'success': True, 'users': users, 'total': len(users)}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# ════════════ HEALTH CHECK ════════════

@app.route('/api/health', methods=['GET'])
def health():
    db_type = 'PostgreSQL' if 'postgresql' in app.config['SQLALCHEMY_DATABASE_URI'] else 'SQLite'
    return jsonify({
        'status': 'Backend is running',
        'database': db_type,
        'timestamp': str(datetime.now())
    }), 200

# ════════════ ERROR HANDLERS ════════════

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'message': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({'success': False, 'message': 'Internal server error'}), 500


# ════════════ MAIN ENTRY POINT ════════════

if __name__ == '__main__':
    print("🚀 Backend starting on Render...")
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)