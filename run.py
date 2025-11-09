"""
Bus Depot Management System
Application entry point
"""

# FIXED: Import create_app first, then conditionally import socketio
from app import create_app, SOCKETIO_ENABLED
from app.models import db

# Create Flask application instance
app = create_app()

# Create database tables if they don't exist
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == '__main__':
    print("=" * 60)
    print("Bus Depot Management System")
    print("=" * 60)
    print("Starting Flask development server...")
    print("Access the application at: http://localhost:5000")
    print("Press CTRL+C to quit")
    print("=" * 60)

    if SOCKETIO_ENABLED:
        # Import socketio AFTER app creation to avoid circular imports
        from app import socketio
        socketio.run(app, debug=True, host='0.0.0.0', port=5000)
    else:
        # Fallback to regular Flask
        print("⚠️ Running without Socket.IO - install dependencies for full features")
        app.run(debug=True, host='0.0.0.0', port=5000)
