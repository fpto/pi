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

gpioList = [26, 19, 13, 06, 12, 16, 20, 21]

for i in gpioList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Sleep time variables

sleepTimeShort = 0.2
sleepTimeLong = 0.1

# MAIN LOOP =====
# ===============
def job():
    try:
        for i in gpioList:
            GPIO.output(i, GPIO.LOW)
            time.sleep(sleepTimeShort);
            GPIO.output(i, GPIO.HIGH)
            time.sleep(sleepTimeLong);

    except KeyboardInterrupt:
        print " Quit"
        GPIO.cleanup()

schedule.every().minute.do(job)

while True:
    schedule.run_pending()

