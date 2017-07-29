from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('controller move')
def handle_controller_move(arg1):
    print('received args: ' + arg1)

if __name__ == '__main__':
    socketio.run(app)
