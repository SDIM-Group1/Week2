import smbus
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
pwm_led = GPIO.PWM(11, 500)
pwm_led.start(100)

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)
while True:
    GPIO.output(11, True)
    bus.write_byte(address,A3)
    value = bus.read_byte(address) -60
    if value <60:
        pwm_led.ChangeDutyCycle(0)
        time.sleep(0.01)
    else:
        pwm_led.ChangeDutyCycle(value)
        time.sleep(0.01)
    print("当前温度:%1.0f  ℃ " %(value))
    time.sleep(0.1)
    GPIO.output(11, False)

