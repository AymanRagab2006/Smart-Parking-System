import RPi.GPIO as GPIO
import time

blue_led = 23
ldr = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(ldr, GPIO.IN)

while True:
    if GPIO.input(ldr) == 1:
        GPIO.output(blue_led, GPIO.HIGH)
    elif GPIO.input(ldr) == 0:
        GPIO.output(blue_led, GPIO.LOW)
    time.sleep(1)


