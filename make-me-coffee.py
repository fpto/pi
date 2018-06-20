#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import schedule

GPIO.setmode(GPIO.BCM)

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

i = 26

GPIO.setup(i, GPIO.OUT)

# Sleep time variables

brewingTime = 10

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

schedule.every().minute.do(job)

while True:
    schedule.run_pending()
