import time

import RPi.GPIO as GPIO

# GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    i = GPIO.input(channel)
    print(i)
    if i:
        print("Some water")


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
    time.sleep(1)
    callback(channel)
