import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep  # Import the sleep function from the time module

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.cleanup()
GPIO.setup(40, GPIO.OUT)  # Set pin 8 to be an output pin and set initial value to low (off)
while True:  # Run forever
    print("Turn on")
    GPIO.output(40, 1)  # Turn on
    sleep(1)  # Sleep for 1 second
    print("Turn off")
    GPIO.output(40, 0)  # Turn off
    sleep(1)  # Sleep for 1 second
