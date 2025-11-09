import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Disable background tasks during migration
os.environ['SKIP_BACKGROUND_TASKS'] = '1'

# FIXED: Use create_app() pattern
from app import create_app
from app.models import db
from sqlalchemy import text, inspect

app = create_app()

def safe_add_column(table, column, column_type, default=None):
    """Add column only if it doesn't exist"""
    inspector = inspect(db.engine)
    columns = [col['name'] for col in inspector.get_columns(table)]

    if column not in columns:
        default_clause = f" DEFAULT {default}" if default else ""
        query = f"ALTER TABLE {table} ADD COLUMN {column} {column_type}{default_clause}"
        db.session.execute(text(query))
        print(f"✅ Added {table}.{column}")
    else:
        print(f"ℹ️ {table}.{column} already exists")

with app.app_context():
    try:
        # First, create all tables if they don't exist
        print("Creating database tables if they don't exist...")
        db.create_all()
        print("✅ Database tables ready\n")

        # Now add GPS columns
        print("Adding GPS tracking columns...")
        safe_add_column('buses', 'location_lat', 'REAL', '18.5204')
        safe_add_column('buses', 'location_lng', 'REAL', '73.8567')
        safe_add_column('buses', 'last_location_update', 'DATETIME')
        safe_add_column('buses', 'current_speed', 'REAL', '0.0')
        safe_add_column('buses', 'is_active', 'BOOLEAN', '0')

        db.session.commit()
        print("\n✅ Database migration completed successfully!")

    except Exception as e:
        db.session.rollback()
        print(f"\n❌ Migration error: {e}")
        print("Tip: This is normal if columns already exist.")
