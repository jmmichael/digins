'''
http://apprize.info/hardware/raspberry/12.html
The variable led_state contains the current state of the LED (True for On and False for Off). Whenever the button is pressed,
the following line is run:
led_state = notled_state

The not command inverts the value of led_state, so if led_state is True, it becomes False and vice versa.
The variable old_input_state is used to remember the button position so that a button press is defined as occurring only
when the input state changes from being True (switch not pressed) to False (switch pressed).

'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

switch_pin = 16
led_pin = 18

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

led_state = False

old_input_state = True # pulled-up

while True:
    new_input_state = GPIO.input(switch_pin)

    if new_input_state == False and old_input_state == True:

        led_state = not led_state

    old_input_state = new_input_state

    GPIO.output(led_pin, led_state)
