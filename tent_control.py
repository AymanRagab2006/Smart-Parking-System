import RPi._GPIO as GPIO
from BlynkLib import Blynk
import adafruit_dht
import board
import time

BlYNK_AUTH = "FrG6_tvF2KEY3Chu5THFkLYhLMZ8E_DK"

blynk = Blynk(BlYNK_AUTH, server='blynk.cloud', port=80)

tent_servo = 12



GPIO.setmode(GPIO.BCM)
GPIO.setup(tent_servo, GPIO.OUT)

tent = GPIO.PWM(tent_servo, 50)
dht = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temp_c = dht.temperature
        print(temp_c)
        if temp_c > 28:
            dht.start(0)
            dht.ChangeDutyCucle(12)
        else:
            dht.start(0)
            dht.ChangeDutyCycle(2)

        blynk.virtual_write(1, temp_c)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1)
    except Exception as error:
        dht.exit()
        raise error
    blynk.run()
    time.sleep(10)