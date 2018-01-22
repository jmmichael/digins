'''
http://apprize.info/hardware/raspberry/12.html
Once triggered, the output of the PIR sensor will stay high for a little while.
Adjust this using one of the trimpots on its circuit board.

'''
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)

while True:

    input_state = GPIO.input(18)

    if input_state == True:

        print('Motion Detected')

        time.sleep(1)
