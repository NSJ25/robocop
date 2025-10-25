from main import pin

def getRightWheel():
    wheels = [pin[0],pin[1]] # Mettre les pins des roues droites ⚠️
    return wheels

def getLeftWheel():
    wheels = [pin[2],pin[3]] # Mettre les pins des roues gauches ⚠️
    return wheels

def getAllWheel():
    wheels = getRightWheel() + getLeftWheel()
    return wheels


def getPinLed():
    return [pin[4],pin[5]] # Mettre les pins du led ⚠️ C'est juste un exemple, mettez les numéros correctes.