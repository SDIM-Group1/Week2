import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(11, RPi.GPIO.OUT)
pwm = RPi.GPIO.PWM(11, 80)

pwm.start(0)

try:
    while True:
        for i in xrange(0, 101, 1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)
            for i in xrange(100, -1, -1):
                pwm.ChangeDutyCycle(i)
                time.sleep(.02)

except KeyboardInterrupt:
    pass

pwm.stop()

RPi.GPIO.cleanup()