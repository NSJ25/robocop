from main import pin

def getRightWheel():
    wheels = [pin[0],pin[1]]
    return wheels

def getLeftWheel():
    wheels = [pin[2],pin[3]]
    return wheels

def getAllWheel():
    wheels = getRightWheel() + getLeftWheel()
    return wheels