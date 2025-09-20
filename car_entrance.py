import RPi.GPIO as GPIO
from BlynkLib import Blynk
import time

BlYNK_AUTH = "FrG6_tvF2KEY3Chu5THFkLYhLMZ8E_DK"

blynk = Blynk(BlYNK_AUTH, server='blynk.cloud', port=80)

trigger_pin_entrance = 15
echo_pin_entrance = 14
trigger_pin_exit = 24
echo_pin_exit = 23
gate_entarnce_servo = 18
gate_exit_servo = 21
"""red_led = 21
yellow_led = 20
green_led = 16"""

available_slots = 9


GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin_entrance, GPIO.OUT)
GPIO.setup(echo_pin_entrance, GPIO.IN)
GPIO.setup(trigger_pin_exit, GPIO.OUT)
GPIO.setup(echo_pin_exit, GPIO.IN)
GPIO.setup(gate_entarnce_servo, GPIO.OUT)
GPIO.setup(gate_exit_servo, GPIO.OUT)

"""GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)"""

gate_entrance = GPIO.PWM(gate_entarnce_servo, 50)
gate_exit = GPIO.PWM(gate_exit_servo, 50)

GPIO.output(trigger_pin_entrance, GPIO.LOW)
GPIO.output(trigger_pin_exit, GPIO.LOW)
"""GPIO.output(red_led, GPIO.LOW)
GPIO.output(yellow_led, GPIO.LOW)
GPIO.output(green_led, GPIO.LOW)"""

time.sleep(2)

def get_distance(trig, echo):
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)

    while GPIO.input(echo) == 0:
        start_pulse = time.time()
    while GPIO.input(echo) == 1:
        end_pulse = time.time()

    pulse_duration = end_pulse - start_pulse
    distance = (pulse_duration * 34300) / 2
    return distance

while True:

    #print("hello")

    dist_entrance = get_distance(trigger_pin_entrance, echo_pin_entrance)
    print(dist_entrance)

    dist_exit = get_distance(trigger_pin_exit, echo_pin_exit)
    print(dist_exit)

    if dist_entrance < 10 and available_slots > 0:
        print(available_slots)
        available_slots -= 1
        gate_entrance.start(0)
        gate_entrance.ChangeDutyCycle(7) 
        print("Entrance Gate opened")
        """GPIO.output(yellow_led,GPIO.LOW)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.HIGH)"""
        time.sleep(2)
        """GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.LOW)
        GPIO.output(yellow_led,GPIO.HIGH)"""
        blynk.virtual_write(0, available_slots)
        lcd.write_text("Slots: " + str(available_slots), 1)

        gate_entrance.start(0)
        gate_entrance.ChangeDutyCycle(2)
    


    if dist_exit < 10:
        print(available_slots)
        available_slots += 1
        gate_exit.start(0)
        gate_exit.ChangeDutyCycle(7) 
        print("Exit Gate opened")
        """GPIO.output(yellow_led,GPIO.LOW)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.HIGH)"""
        time.sleep(2)
        """GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.LOW)
        GPIO.output(yellow_led,GPIO.HIGH)"""
        blynk.virtual_write(0, available_slots)

        lcd.write_text("Slots: " + str(available_slots), 1)

        gate_exit.start(0)
        gate_exit.ChangeDutyCycle(2)
    

    
    blynk.run()

    
    time.sleep(0.1)
