import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm_led = GPIO.PWM(11, 500)
pwm_led.start(100)
while True:
    GPIO.output(11, True)
    pwm_led.ChangeDutyCycle(0)
    time.sleep(2)
    pwm_led.ChangeDutyCycle(50)
    time.sleep(2)
    pwm_led.ChangeDutyCycle(100)
    time.sleep(1)
    GPIO.output(11, False)
GPIO.cleanup()