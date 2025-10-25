from machine import Pin
from utime import sleep
from python.controls import JsOnClick

#  ⚠️ Message important ⚠️
# Instruction par rapport aux pins au cas où je vais dormir et vous devriez continuer le projet,
# mettre les pins des roues droites et gauches dans les fonctions getRightWheel() et getLeftWheel() dans pins.py.
# Exemple: pin = [Pin(0),Pin(1),Pin(2),Pin(3)]
# Aussi pas oublier de repertorier les pins existantes dans la liste "pin" ci-dessous. :)

pin = [Pin(0),Pin(1),Pin(2),Pin(3)] # Mettre les pins existantes ici ⚠️
dir = 0
isPressed = False

def press(direction): # ⚠️ Ca doit se jouer quand on appuie sur un bouton il va envoyer un numéro de direction, voir controls.py 
    global dir, isPressed
    dir = direction
    isPressed = True

def release(): # ⚠️ Ca doit se jouer quand on relâche le bouton
    global isPressed
    isPressed = False
    
def init():
    initPin()

def initPin():
    for x in pin:
        x.off()
        x.init(Pin.OUT)

def main_loop():
    if(isPressed):
        JsOnClick(dir)

init()

while 1:
    main_loop()
    sleep(0.01)