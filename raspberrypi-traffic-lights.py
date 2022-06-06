import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) #red
GPIO.setup(27, GPIO.OUT) #yellow
GPIO.setup(22, GPIO.OUT) #green

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #button

GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.output(22,GPIO.HIGH) #green light always on

while True:
    if GPIO.input(23) == GPIO.HIGH:
        print("Button pushed")
        time.sleep(0.5)
        pedestrian()
        time.sleep(15)

def pedestrian():
    #go from green to yellow
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(3)
    
    #go from yellow to red
    GPIO.output(27, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(8)
    
    #red back to green
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(3)