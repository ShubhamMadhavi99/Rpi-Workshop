import RPi.GPIO as GPIO
import time
import os, sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#setup output pins
GPIO.setup(35, GPIO.OUT)      #//GPIO19
GPIO.setup(12, GPIO.OUT)      #//GPIO18
GPIO.setup(36, GPIO.OUT)      #//GPIO16
GPIO.setup(33, GPIO.OUT)      #//GPIO13
GPIO.setup(32, GPIO.OUT)      #//GPIO12
GPIO.setup(38, GPIO.OUT)      #//GPIO20
GPIO.setup(40, GPIO.OUT)      #//GPIO21

#define 7 segment digits
digitclr=[1,1,1,1,1,1,1]
digit0=[1,1,1,1,1,1,0]
digit1=[0,1,1,0,0,0,0]
digit2=[1,1,0,1,1,0,1]
digit3=[1,1,1,1,0,0,1]
digit4=[0,1,1,0,0,1,1]
digit5=[1,0,1,1,0,1,1]
digit6=[1,0,1,1,1,1,1]
digit7=[1,1,1,0,0,0,0]
digit8=[1,1,1,1,1,1,1]
digit9=[1,1,1,0,0,1,1]
gpin=[35,12,36,33,32,38,40]

#routine to clear and then write to display
def digdisp(digit):
    for x in range (0,7):
        GPIO.output(gpin[x], digitclr[x])
    for x in range (0,7):
        GPIO.output(gpin[x], digit[x])

#routine to display digit from 0 to 9
digdisp(digit0)
time.sleep(1)
digdisp(digit1)
time.sleep(1)
digdisp(digit2)
time.sleep(1)
digdisp(digit3)
time.sleep(1)
digdisp(digit4)
time.sleep(1)
digdisp(digit5)
time.sleep(1)
digdisp(digit6)
time.sleep(1)
digdisp(digit7)
time.sleep(1)
digdisp(digit8)
time.sleep(1)
digdisp(digit9)
time.sleep(1)
#tidy up
GPIO.cleanup()
import sys
sys.exit()
