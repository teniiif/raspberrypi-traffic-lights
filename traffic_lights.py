from gpiozero import LED, Button
from time import sleep
from signal import pause

red = LED(17)
yellow = LED(27)
green = LED(22)

button = Button(23)

red.off()
yellow.off()
green.on()

def pedestrian():
    #go from green to yellow
    green.off()
    yellow.on()
    sleep(5)
    #go from yellow to red
    yellow.off()    
    red.on()
    sleep(15)
    red.off()
    green.on()

    
while True:
    button.when_pressed = pedestrian
    sleep(15)