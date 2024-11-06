from hcsr04 import HCSR04
from time import sleep, ticks_ms
from machine import Pin, PWM

#rød
led1 = Pin(26, Pin.OUT)
led1_PWM = PWM(led1)


# Creates an instance of the HCSR04 class
sensor = HCSR04(15,34)

# Starttiden?
start = ticks_ms()

# Periode der ventes i millisekunder
threshold_ms = 100

# Starts the event loop
while True:
     if ticks_ms() - start > threshold_ms:
        # Calls the distance_cm method and
        # stores the return value in the variable distance
        distance = int(sensor.distance_cm())
        led1_PWM.duty(distance)
        print('Distance:', round(distance,2), 'cm')
        start = ticks_ms()