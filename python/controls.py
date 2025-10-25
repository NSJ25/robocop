from utils import isInRange
from machine import PWM
from python.pins import *

maxSpeed = 65000

def JsOnClick(direction):
    # 0 = forward
    # 1 = backward
    # 2 = left
    # 3 = right

    speed = 0
    freq = 100

    if isInRange(direction, 0, 1): # forward or backward
        if direction == 0:
            speed = maxSpeed
        elif direction == 1:
            speed = -maxSpeed

        wheels = getAllWheel()
        for wheel in wheels:
            pwm = PWM(wheel)
            pwm.freq(freq)
            pwm.duty_u16(speed)

    elif isInRange(direction, 2, 3): # left or right
        if direction == 2:
            leftSpeed = -maxSpeed
            rightSpeed = maxSpeed
        elif direction == 3:
            leftSpeed = maxSpeed
            rightSpeed = -maxSpeed

        leftWheels = getLeftWheel()
        rightWheels = getRightWheel()

        for wheel in leftWheels:
            pwm = PWM(wheel)
            pwm.freq(freq)
            pwm.duty_u16(leftSpeed)

        for wheel in rightWheels:
            pwm = PWM(wheel)
            pwm.freq(freq)
            pwm.duty_u16(rightSpeed)
