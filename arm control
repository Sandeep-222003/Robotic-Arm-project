from flask import Flask, request
import pigpio
from adafruit_pca9685 import PCA9685
import board, busio

app = Flask(__name__)

# Servo driver setup
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50

def set_servo(channel, angle):
    pwm_min = 1000
    pwm_max = 2000
    pulse = pwm_min + (angle/180)*(pwm_max-pwm_min)
    pca.channels[channel].duty_cycle = int(pulse * 16.5)

@app.route("/servo/<int:ch>/<int:angle>")
def servo_control(ch, angle):
    set_servo(ch, angle)
    return "OK"

@app.route("/move/<direction>")
def move(direction):
    # Here you send signals to SmartElex motor driver
    if direction == "forward":
        # GPIO control code
        pass
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
