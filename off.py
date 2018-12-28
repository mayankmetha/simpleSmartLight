import RPi.GPIO as GPIO
import time
import ADC0832

pinsLed = {'R':11,'G':12,'B':13}

p_R = GPIO.PWM(pinsLed['R'],2000)
p_G = GPIO.PWM(pinsLed['G'],2000)
p_B = GPIO.PWM(pinsLed['B'],5000)

p_R.stop()
p_G.stop()
p_B.stop()
for i in pinsLed:
    GPIO.output(pinsLed[i],GPIO.LOW)
GPIO.cleanup()
ADC0832.destroy()