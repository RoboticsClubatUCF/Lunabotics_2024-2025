import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin_list = [12, 13, 18]
GPIO.setup(pin_list, GPIO.OUT)

#Initialize controllers
left_pwm_controller = GPIO.PWM(12, 50)
right_pwm_controller = GPIO.PWM(13, 50)
intake_pwm_controller = GPIO.PWM(18, 50)

#Set inital duty cycle
left_pwm_controller.start(0.0)
right_pwm_controller.start(0.0)
intake_pwm_controller.start(0.0)

while True:
    speed = float(input("speed (-1 to 1): "))
    right_pwm_controller.ChangeDutyCycle(7.5 + (speed * 2.5))
    left_pwm_controller.ChangeDutyCycle(7.5 + (speed * 2.5))
    intake_pwm_controller.ChangeDutyCycle(7.5 + (speed * 2.5))
