import serial
import time

# Setup serial communication (GPIO 14 is the TX pin)
ser = serial.Serial(
    "/dev/serial0",  # Serial port for UART (GPIO 14 is TX)
    baudrate=9600,   # Sabertooth's default baud rate
    timeout=1
)

def send_motor_command(motor, speed):
    """
    Send a command to control a motor via the Sabertooth in Simplified Serial Mode.
    
    motor: 1 or 2
    speed: Integer from -127 to 127 where:
        -127 is full reverse
        0 is stop
        127 is full forward
    """
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
    else:
        raise ValueError("Motor must be 1 or 2")
    
    ser.write(bytes([command]))

def stop_motors():
    """
    Stop both motors by sending 0x00.
    """
    ser.write(bytes([0x00]))

while(true)
	x=input("Speed: ")
	send_motor_command(1, x)
	send_motor_command(2, x)


