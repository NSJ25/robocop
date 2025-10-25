from machine import Pin
from utime import sleep

pin = [Pin(0),Pin(1),Pin(2),Pin(3)]

def init():
    initPin()

def initPin():
    for x in pin:
        x.off()
        x.init(Pin.OUT)

def main_loop():
    pass

init()

while 1:
    main_loop()