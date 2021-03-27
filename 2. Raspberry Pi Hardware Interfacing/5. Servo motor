import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

pwm=GPIO.PWM(7, 50)
pwm.start(0)


def SetAngle(angle):
    	duty = int(angle) / 18 + 2
    	GPIO.output(7, True)
    	pwm.ChangeDutyCycle(duty)
    	sleep(1)
    	GPIO.output(7, False)
    	pwm.ChangeDutyCycle(0)

angle = input('Enter the angle in degrees:')
SetAngle(angle)
pwm.stop()
GPIO.cleanup()
    		
