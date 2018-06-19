import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
try:
	while True:
		GPIO.output(3, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(3, GPIO.LOW)
		time.sleep(0.5)


except KeyboardInterrupt:
    print " Quit"

    # Reset GPIO settings

    GPIO.cleanup()
