import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.OUT)

print("Testing RF out, Press CTRL+C to exit")

try:
     print("set GIOP high")
     GPIO.output(11, GPIO.HIGH)
     time.sleep(5)
except KeyboardInterrupt:
   print("Keyboard interrupt")

except:
   print("some error")

finally:
   print("clean up")
   GPIO.cleanup()
