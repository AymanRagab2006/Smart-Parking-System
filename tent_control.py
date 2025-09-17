import RPi._GPIO as GPIO
import adafruit_dht
import board
import time

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

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1)
    except Exception as error:
        dht.exit()
        raise error
    time.sleep(1)