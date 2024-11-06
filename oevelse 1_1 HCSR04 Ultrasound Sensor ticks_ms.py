from hcsr04 import HCSR04
from time import sleep, ticks_ms
from machine import Pin, PWM

#rød
led1 = Pin(26, Pin.OUT)
led1_start = ticks_ms()
led1_period = 500

# Creates an instance of the HCSR04 class
sensor = HCSR04(15,34)

# Starttiden?
start_time = ticks_ms()

# Periode der ventes i millisekunder
threshold_ms = 100

# Starts the event loop
while True:
     if ticks_ms() - start_time > threshold_ms:
        # Calls the distance_cm method and
        # stores the return value in the variable distance
        distance = sensor.distance_cm()
        print('Distance:', round(distance,2), 'cm')
        start_time = ticks_ms()

