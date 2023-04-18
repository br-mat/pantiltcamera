from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import json

class ServoController:
    def __init__(self, servo_pin, direction):
        # Initialize GPIO and servo motor
        self.factory = PiGPIOFactory()
        self.servo = Servo(servo_pin, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory)
        
        # Store the direction and position
        self.dir = direction.lower()
        self.position_file = '/home/youruser/pantiltcamera/src/position.json'
        self.position = self.load_position()

    def move(self, angle):
        # Limit angle
        angle = max(min(angle, 180), 0)
        
        # Convert angle to value and move servo
        value = (angle / 180.0) * 2 - 1
        self.servo.value = value
        time.sleep(0.5)
        
        # Update and save the new position
        self.position = angle
        self.save_position()

    def load_position(self):
        # Load the position from the file for the given direction
        try:
            with open(self.position_file, 'r') as f:
                return json.load(f)[self.dir]
        except FileNotFoundError:
            return 0

    def save_position(self):
        # Save the position to the file for the given direction
        with open(self.position_file, 'w') as f:
            json.dump({self.dir: self.position}, f)
            
    def up(self):
        # Move the servo up by decreasing the position by 10
        self.position -= 15
        self.move(self.position)

    def down(self):
        # Move the servo down by increasing the position by 10
        self.position += 15
        self.move(self.position)

    def cleanup(self):
        # Stop the servo motor and clean up GPIO pins
        self.servo.detach()
        self.factory.close()
