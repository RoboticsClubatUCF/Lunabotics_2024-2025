#!/usr/bin/env python3
import serial
import RPi.GPIO as GPIO
#pin 6 GPIO 22

ser = serial.Serial(
    "/dev/serial0", # Serial port for UART (GPIO 14 is TX)
    baudrate=9600, # Sabertooth's default baud rate
    timeout=1
)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)

def motor_command(motor, speed):
    if motor == 1:
        command = speed + 64  # Map to 1â€“127 for motor 1
        if command < 1:
            command = 1
        elif command > 127:
            command = 127
    elif motor == 2:
        command = speed + 192  # Map to 128â€“255 for motor 2
        if command < 128:
            command = 128
        elif command > 255:
            command = 255
    ser.write(bytes([command]))


while True:
    x = int(input("Speed (-127 to 127): "))
    motor_command(1, x)
    motor_command(2, x)
