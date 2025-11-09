import os
from flask import Flask, render_template, session, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import Config
from app.models import db
from app.translations import get_translation

csrf = CSRFProtect()

# Conditional Socket.IO import
try:
    from flask_socketio import SocketIO
    socketio = SocketIO()
    SOCKETIO_ENABLED = True
except ImportError:
    socketio = None
    SOCKETIO_ENABLED = False

def create_app(config_class=Config):
    """Flask application factory"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    # Only initialize Socket.IO if available
    # FIXED: Use threading mode for SQLite compatibility
    if SOCKETIO_ENABLED:
        socketio.init_app(app,
                         cors_allowed_origins="*",
                         async_mode='threading',
                         logger=False,
                         engineio_logger=False)
        print("✅ Socket.IO initialized (threading mode)")
    else:
        print("⚠️ Socket.IO not available - real-time features disabled")

    # Register blueprints
    from app.blueprints.home import home_bp
    from app.blueprints.buses import buses_bp
    from app.blueprints.routes import routes_bp
    from app.blueprints.schedules import schedules_bp
    from app.blueprints.crew import crew_bp
    from app.blueprints.dashboard import dashboard_bp
    from app.blueprints.reports import reports_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(buses_bp, url_prefix='/buses')
    app.register_blueprint(routes_bp, url_prefix='/routes')
    app.register_blueprint(schedules_bp, url_prefix='/schedules')
    app.register_blueprint(crew_bp, url_prefix='/crew')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(reports_bp, url_prefix='/reports')

    # Start background tasks if Socket.IO available and not skipped
    skip_background = os.environ.get('SKIP_BACKGROUND_TASKS', '0') == '1'
    if SOCKETIO_ENABLED and not skip_background:
        from app.blueprints.dashboard import background_tasks
        background_tasks.start_background_updates(app)

        # Import socket_events to register event handlers
        from app.blueprints.dashboard import socket_events
    elif skip_background:
        print("⚠️ Background tasks skipped (migration mode)")

    # Language switching route
    @app.route('/set-language/<lang>')
    def set_language(lang):
        """Set user's language preference"""
        if lang in ['en', 'mr']:
            session['lang'] = lang
        return redirect(request.referrer or url_for('home.index'))

    # Context processor for translations
    @app.context_processor
    def inject_translations():
        """Make translation function available in all templates"""
        lang = session.get('lang', 'en')
        def t(key):
            return get_translation(key, lang)
        return dict(t=t, current_lang=lang)

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    return app
