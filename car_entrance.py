import RPi.GPIO as GPIO
import time

trigger_pin = 6
echo_pin = 5
gate_servo = 12
red_led = 21
yellow_led = 20
green_led = 16

available_slots = 9


GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(gate_servo, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

gate = GPIO.PWM(gate_servo, 50)

GPIO.output(trigger_pin, GPIO.LOW)
time.sleep(2)


def get_distance():
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == 0:
        start_pulse = time.time()
    while GPIO.input(echo_pin) == 1:
        end_pulse = time.time()

    pulse_duration = end_pulse - start_pulse
    distance = (pulse_duration * 34300) / 2
    return distance

while True:
    print("hello")
    dist = get_distance()
    print(dist)
    if dist < 10 and available_slots > 0:
        # TODO: open gate 

        print(available_slots)
        available_slots -= 1
        gate.start(0)
        gate.ChangeDutyCycle(7) 
        print("Gate opened")
        GPIO.output(yellow_led,GPIO.LOW)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.LOW)
        GPIO.output(yellow_led,GPIO.HIGH)
    else:
        gate.start(0)
        gate.ChangeDutyCycle(2)
        print("Gate closed")
        GPIO.output(green_led, GPIO.LOW)
        GPIO.output(yellow_led,GPIO.LOW)
        GPIO.output(red_led, GPIO.HIGH)

    
    time.sleep(1)

