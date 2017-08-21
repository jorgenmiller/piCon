from flask import Flask, render_template
from flask_socketio import SocketIO
from BrickPi import *

BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1



app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('button')
def handle_controller_move(arg1):
    print('received args: ' + arg1)
    BrickPi.MotorSpeed[PORT_A] = str(arg1)
    BrickPiUpdateValues()

if __name__ == '__main__':
    socketio.run(app,host= '0.0.0.0')
