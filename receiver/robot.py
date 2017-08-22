from flask import Flask, render_template
from flask_socketio import SocketIO
from BrickPi import *

BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1
BrickPi.MotorEnable[PORT_D] = 1

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on("button", "motor A")
def handle_button(arg2):
    print('received args: ' + arg2)
    BrickPi.MotorSpeed[PORT_A] = int(arg1)
    BrickPiUpdateValues()
    BrickPiUpdateValues()

if __name__ == '__main__':
    socketio.run(app,host= '0.0.0.0')
