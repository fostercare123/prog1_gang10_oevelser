from hcsr04 import HCSR04
from time import sleep, ticks_ms

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
