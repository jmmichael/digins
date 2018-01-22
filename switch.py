'''
When the swich is pressed, it will connect pin 16 configured as an input to GND. The input pin is normally pulled up to 3.3V
by the optional argument pull_up_down=GPIO.PUD_UP in GPIO.setup. This means that when you read the input value using GPIO.input,
False will be returned if the button is pressed. This is a little counterintuitive.
Each GPIO pin has software configurable pull-up and pull-down resistors.
When using a GPIO pin as an input, you can configure these resistors so that one or either or neither of the resistors is
enabled, using the optional pull_up_down parameter to GPIO.setup. If this parameter is omitted, then neither resistor
will be enabled. This leaves the input floating, which means that its value cannot be relied upon and it will drift
between high and low depending on what it picks up in the way of electrical noise.
If it is set to GPIO.PUD_UP, the pull-up resistor is enabled; if it is set to GPIO.PUD_DOWN, the pull-down resistor is enabled.


'''
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

    input_state = GPIO.input(16)

    if input_state == False:

        print('Button Pressed')

        time.sleep(0.2)
