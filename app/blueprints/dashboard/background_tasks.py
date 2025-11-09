import threading
import time
import random
from datetime import datetime
from sqlalchemy.exc import OperationalError

def start_background_updates(app):
    """Start background thread for bus location updates"""

    def update_bus_locations():
        while True:
            try:
                with app.app_context():
                    from app import db, socketio, SOCKETIO_ENABLED
                    from app.models import Bus

                    active_buses = Bus.query.filter_by(is_active=True).all()

                    for bus in active_buses:
                        # Simulate GPS movement (±0.001 degrees ≈ 100m)
                        bus.location_lat += random.uniform(-0.001, 0.001)
                        bus.location_lng += random.uniform(-0.001, 0.001)
                        bus.current_speed = random.uniform(20, 60)
                        bus.last_location_update = datetime.utcnow()

                        # Emit update if Socket.IO available
                        if SOCKETIO_ENABLED:
                            socketio.emit('bus_update', {
                                'bus_id': bus.id,
                                'bus_number': bus.registration_number,
                                'lat': bus.location_lat,
                                'lng': bus.location_lng,
                                'speed': bus.current_speed
                            }, namespace='/')

                    # FIXED: SQLite-safe commit with retry
                    try:
                        db.session.commit()
                    except OperationalError as e:
                        if "database is locked" in str(e):
                            db.session.rollback()
                            time.sleep(1)  # Wait and retry
                            try:
                                db.session.commit()
                            except:
                                pass  # Skip this update cycle
                        else:
                            raise

            except Exception as e:
                print(f"Background task error: {e}")
                try:
                    db.session.rollback()
                except:
                    pass

            time.sleep(5)  # Update every 5 seconds

    # Start daemon thread
    thread = threading.Thread(target=update_bus_locations, daemon=True)
    thread.start()
    print("✅ Background bus update thread started")
