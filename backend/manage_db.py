#!/usr/bin/env python3
"""Database Management Tool for IndustrySolve"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db
from models import User

def show_all_users():
    """Display all users in database"""
    with app.app_context():
        users = User.query.all()
        if not users:
            print("\n📭 No users found in database.\n")
            return
        
        print("\n📊 IndustrySolve Users Database:")
        print("=" * 130)
        print(f"{'Email':<30} {'Name':<20} {'Role':<10} {'College/Org':<25} {'Domain/Industry':<20} {'Created At':<20}")
        print("=" * 130)
        
        for user in users:
            college_org = user.college or user.org_name or '—'
            domain_ind = user.domain or user.industry or '—'
            created = user.created_at.strftime('%Y-%m-%d %H:%M:%S')
            print(f"{user.email:<30} {user.name:<20} {user.role:<10} {college_org:<25} {domain_ind:<20} {created:<20}")
        
        print("=" * 130)
        print(f"\n✅ Total Users: {len(users)}\n")

def delete_all_users():
    """Clear all users from database"""
    with app.app_context():
        count = User.query.count()
        if count == 0:
            print("\n📭 Database is already empty.\n")
            return
        
        confirm = input(f"⚠️  Delete all {count} users? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                db.drop_all()
                db.create_all()
                print(f"✅ Deleted {count} users. Database reset.\n")
            except Exception as e:
                print(f"❌ Error: {e}\n")
        else:
            print("❌ Cancelled.\n")

def get_database_stats():
    """Show database statistics"""
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    
    print("\n📊 Database Statistics:")
    print("=" * 50)
    
    if 'sqlite' in db_uri:
        db_path = db_uri.replace('sqlite:///', '')
        if os.path.exists(db_path):
            file_size = os.path.getsize(db_path)
            file_size_mb = file_size / (1024 * 1024)
            print(f"Database Type: SQLite")
            print(f"Database File: {os.path.abspath(db_path)}")
            print(f"File Size: {file_size:,} bytes ({file_size_mb:.2f} MB)")
        else:
            print(f"Database Type: SQLite (file not found locally)")
    else:
        # For Postgres/other remote DBs
        db_type = db_uri.split(':')[0]
        print(f"Database Type: {db_type.upper()}")
        print(f"Database Status: Remote Connection")
    
    with app.app_context():
        try:
            user_count = User.query.count()
            print(f"Total Users: {user_count}")
        except Exception as e:
            print(f"Error fetching user count: {e}")
            
    print("=" * 50)
    print()

def main():
    print("\n🔧 IndustrySolve Database Manager\n")
    
    options = {
        '1': ('Show All Users', show_all_users),
        '2': ('Database Statistics', get_database_stats),
        '3': ('Reset Database (Delete All Users)', delete_all_users),
        '4': ('Exit', None)
    }
    
    while True:
        print("Options:")
        for key, (label, _) in options.items():
            print(f"  {key}) {label}")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '4':
            print("\n👋 Goodbye!\n")
            break
        
        if choice in options:
            _, func = options[choice]
            if func:
                func()
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == '__main__':
    try:
        print("Connecting to database...")
        # Check if database is accessible
        with app.app_context():
            db.engine.connect()
            print("✅ Database connection established.")
        main()
    except Exception as e:
        print(f"\n❌ Database Connection Error: {e}")
        print("Make sure your DATABASE_URL is correct and the database is accessible.\n")
