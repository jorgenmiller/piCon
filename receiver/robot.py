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

@socketio.on("button")
def handle_button(arg1, arg2):
    print(str(arg1) + ": " + str(arg2))
    if arg1 == "motor A":
        BrickPi.MotorSpeed[PORT_A] = int(arg2)
    elif arg1 == "motor B":
            BrickPi.MotorSpeed[PORT_B] = int(arg2)
    elif arg1 == "motor C":
            BrickPi.MotorSpeed[PORT_C] = int(arg2)
    elif arg1 == "motor D":
            BrickPi.MotorSpeed[PORT_D] = int(arg2)
    BrickPiUpdateValues()
    BrickPiUpdateValues()

if __name__ == '__main__':
    socketio.run(app,host= '0.0.0.0')
