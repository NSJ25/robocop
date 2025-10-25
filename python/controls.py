from utils import isInRange
from machine import PWM
from python.pins import *

#  🛞  Ca c'est pour la navigation

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
            #speed = -maxSpeed
            speed = 0  # Pour éviter les problèmes avec le PWM négatif

        wheels = getAllWheel()
        for wheel in wheels:
            pwm = PWM(wheel)
            pwm.freq(freq)
            pwm.duty_u16(speed)

    elif isInRange(direction, 2, 3): # left or right
        if direction == 2:
            #leftSpeed = -maxSpeed
            leftSpeed = 0  # Pour éviter les problèmes avec le PWM négatif
            rightSpeed = maxSpeed
        elif direction == 3:
            leftSpeed = maxSpeed
            #rightSpeed = -maxSpeed
            rightSpeed = 0  # Pour éviter les problèmes avec le PWM négatif

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

#  🚨  Ca c'est pour les leds

def setLedState(state):
    # state = True (allume les leds) or False (éteint les leds)
    ledPins = getPinLed()
    for led in ledPins:
        if state:
            led.on()
        else:
            led.off()