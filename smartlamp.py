#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import ADC0832

def getTime():
    ltime = time.localtime(time.time())
    return (ltime.tm_hour,ltime.tm_min)

on = 0xFFFFFF
off = 0x000000
pinsLed = {'R':11,'G':12,'B':13}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

for i in pinsLed:
    GPIO.setup(pinsLed[i],GPIO.OUT)

p_R = GPIO.PWM(pinsLed['R'],2000)
p_G = GPIO.PWM(pinsLed['G'],2000)
p_B = GPIO.PWM(pinsLed['B'],5000)

p_R.start(0);
p_G.start(0);
p_B.start(0);

def map(x,in_min,in_max,out_min,out_max):
    return(x-in_min)*(out_max-out_min)/(in_max-in_min)+(out_min)

def setColor(col):
    p_R.ChangeDutyCycle(map(((col&0x110000)>>16),0,255,0,100))
    p_G.ChangeDutyCycle(map(((col&0x001100)>>8),0,255,0,100))
    p_B.ChangeDutyCycle(map(((col&0x000011)>>0),0,255,0,100))
    return

print("Current hour is",getTime()[0],":",getTime()[1])
ADC0832.setup()
for i in pinsLed:
    GPIO.output(pinsLed[i],GPIO.HIGH)
try:
    while getTime()[0] <= 23 and getTime()[0] >= 5:
        res = ADC0832.getResult() - 80
        if res < 0:
            res = 0
        if res > 100:
            res = 100
        if res > 65:
            setColor(on)
        else:
            setColor(off)
        time.sleep(0.25)
except KeyboardInterrupt:
    p_R.stop()
    p_G.stop()
    p_B.stop()
    for i in pinsLed:
        GPIO.output(pinsLed[i],GPIO.LOW)
    GPIO.cleanup()
    ADC0832.destroy()
