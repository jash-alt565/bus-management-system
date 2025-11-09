from app import socketio, SOCKETIO_ENABLED

if SOCKETIO_ENABLED:
    from flask_socketio import emit, join_room

    @socketio.on('connect')
    def handle_connect():
        print('✅ Client connected')
        emit('connection_response', {'status': 'connected'})

    @socketio.on('disconnect')
    def handle_disconnect():
        print('❌ Client disconnected')

    @socketio.on('join_operator')
    def handle_join_operator():
        join_room('operators')
        emit('joined', {'room': 'operators'})

    @socketio.on('join_user')
    def handle_join_user(data):
        bus_id = data.get('bus_id')
        join_room(f'bus_{bus_id}')
        emit('joined', {'room': f'bus_{bus_id}'})

else:
    print("⚠️ Socket.IO events not registered - module not available")
