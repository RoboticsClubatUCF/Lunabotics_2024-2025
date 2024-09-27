import RPi.GPIO as GPIO
import time

# GPIO Pin setup
GPIO.setmode(GPIO.BCM)

# Motor 1: controlled by GPIO23
GPIO.setup(23, GPIO.OUT)

# Motor 2: controlled by GPIO24
GPIO.setup(24, GPIO.OUT)

# Set up PWM on the GPIO pins (100Hz PWM frequency)
pwm_motor1 = GPIO.PWM(23, 100)  # Motor 1 (GPIO23)
pwm_motor2 = GPIO.PWM(24, 100)  # Motor 2 (GPIO24)

# Start PWM with 50% duty cycle (motors stopped at 2.5V)
pwm_motor1.start(50)
pwm_motor2.start(50)

try:
    pwm_motor1.ChangeDutyCycle(50)
    time.sleep(2)
    
    # Full M1
    print("Running Motor 1 forward (5V)...")
    pwm_motor1.ChangeDutyCycle(100)  # 100% duty cycle for full forward
    time.sleep(5)

    # Stop M1
    print("Stopping Motor 1 (2.5V)...")
    pwm_motor1.ChangeDutyCycle(50)  # 50% duty cycle to stop the motor
    time.sleep(2)

    # FullR M1
    print("Running Motor 1 reverse (0V)...")
    pwm_motor1.ChangeDutyCycle(0)  # 0% duty cycle for full reverse
    time.sleep(5)

    # Stop M1
    print("Stopping Motor 1 (2.5V)...")
    pwm_motor1.ChangeDutyCycle(50)  # Stop motor (2.5V)
    time.sleep(2)

    # Full M2
    print("Running Motor 2 forward (5V)...")
    pwm_motor2.ChangeDutyCycle(100)  # 100% duty cycle for full forward
    time.sleep(5)

    print("Stopping Motor 2 (2.5V)...")
    pwm_motor2.ChangeDutyCycle(50)  # Stop motor (2.5V)
    time.sleep(2)

    print("Running Motor 2 reverse (0V)...")
    pwm_motor2.ChangeDutyCycle(0)  # 0% duty cycle for full reverse
    time.sleep(5)

    print("Stopping Motor 2 (2.5V)...")
    pwm_motor2.ChangeDutyCycle(50)  # Stop motor (2.5V)

finally:
    # Cleanup GPIO settings
    pwm_motor1.stop()
    pwm_motor2.stop()
    GPIO.cleanup()
