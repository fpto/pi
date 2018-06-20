#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import schedule

GPIO.setmode(GPIO.BOARD)

# GPIO | Relay
#--------------
# 26     01
# 19     02
# 13     03
# 06     04
# 12     05
# 16     06
# 20     07
# 21     08

# initiate list with pin gpio pin numbers

i = 37

GPIO.setup(i, GPIO.OUT)
GPIO.output(i, GPIO.HIGH)

# Sleep time variables

brewingTime = 120
# Fastest is 2 cups in 100 seconds
# Medium is 2 cups in

# MAIN LOOP =====
# ===============
def job():
    try:
	GPIO.output(i, GPIO.LOW)
    time.sleep(brewingTime);
    GPIO.output(i, GPIO.HIGH)

    except KeyboardInterrupt:
        print " Quit"
        GPIO.cleanup()
# Time needs to consider 6 hours difference
schedule.every().day.at("12:30").do(job)

# Led light pin
l = 7
def ledBlick():
    	GPIO.output(l, GPIO.HIGH)
    	time.sleep(0.5)
    	GPIO.output(l, GPIO.LOW)
    	time.sleep(0.5)

while True:
    schedule.run_pending()
    ledBlick()
