from flask import render_template, jsonify
from app.blueprints.dashboard import dashboard_bp
from app.models import Bus, Route, Schedule, Crew, db
from sqlalchemy import func
import json

@dashboard_bp.route('/')
def index():
    """Display analytics dashboard with charts and statistics"""

    # Summary statistics
    total_buses = Bus.query.count()
    total_routes = Route.query.count()
    total_schedules = Schedule.query.count()
    total_crew = Crew.query.count()

    # Bus status breakdown
    active_buses = Bus.query.filter_by(status='active').count()
    inactive_buses = Bus.query.filter(Bus.status != 'active').count()

    # Schedule frequency distribution
    frequency_data = db.session.query(
        Schedule.frequency,
        func.count(Schedule.id)
    ).group_by(Schedule.frequency).all()

    frequency_labels = [item[0].capitalize() for item in frequency_data]
    frequency_counts = [item[1] for item in frequency_data]

    # Route utilization (number of schedules per route)
    route_data = db.session.query(
        Route.route_name,
        func.count(Schedule.id)
    ).join(Schedule).group_by(Route.id, Route.route_name).all()

    route_labels = [item[0] for item in route_data]
    route_counts = [item[1] for item in route_data]

    # Convert to JSON for JavaScript
    frequency_data_json = json.dumps({
        'labels': frequency_labels,
        'data': frequency_counts
    })

    route_data_json = json.dumps({
        'labels': route_labels,
        'data': route_counts
    })

    return render_template(
        'dashboard/index.html',
        total_buses=total_buses,
        total_routes=total_routes,
        total_schedules=total_schedules,
        total_crew=total_crew,
        active_buses=active_buses,
        inactive_buses=inactive_buses,
        frequency_data=frequency_data_json,
        route_data=route_data_json
    )


# ... EXISTING ROUTES REMAIN UNCHANGED ...

def get_bus_number(bus):
    """Helper to get bus identifier - handles both bus_number and registration_number"""
    return getattr(bus, 'bus_number', None) or getattr(bus, 'registration_number', f'Bus-{bus.id}')


@dashboard_bp.route('/operator')
def operator_dashboard():
    """Operator dashboard with live tracking"""
    active_buses = Bus.query.filter_by(is_active=True).all()
    total_buses = Bus.query.count()

    return render_template('dashboard/operator_dashboard.html',
                         active_buses=active_buses,
                         total_buses=total_buses)


@dashboard_bp.route('/user')
def user_dashboard():
    """User dashboard for bus tracking"""
    routes = Route.query.all()
    return render_template('dashboard/user_dashboard.html', routes=routes)


@dashboard_bp.route('/live-demo')
def live_demo():
    """Live demo with simulation"""
    # Activate first 5 buses for demo
    buses = Bus.query.limit(5).all()
    for bus in buses:
        bus.is_active = True
    db.session.commit()

    return render_template('dashboard/live_demo.html', demo_buses=buses)


@dashboard_bp.route('/api/buses/active')
def get_active_buses():
    """API: Get all active buses"""
    buses = Bus.query.filter_by(is_active=True).all()
    return jsonify([{
        'id': bus.id,
        'bus_number': get_bus_number(bus),
        'lat': bus.location_lat or 18.5204,
        'lng': bus.location_lng or 73.8567,
        'speed': bus.current_speed or 0
    } for bus in buses])


@dashboard_bp.route('/api/bus/<int:bus_id>')
def get_bus_details(bus_id):
    """API: Get single bus details"""
    bus = Bus.query.get_or_404(bus_id)
    return jsonify({
        'id': bus.id,
        'bus_number': get_bus_number(bus),
        'lat': bus.location_lat or 18.5204,
        'lng': bus.location_lng or 73.8567,
        'speed': bus.current_speed or 0,
        'is_active': bus.is_active
    })
