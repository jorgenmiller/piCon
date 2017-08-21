from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on("message")
def handle_message(message):
    print("received message: " + message)

@socketio.on("button")
def handle_button(arg1):
    print("received arg: " + arg1)

if __name__ == "__main__":
    socketio.run(app)
