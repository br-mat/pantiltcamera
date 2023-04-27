"""
    ServoControllerClass this code should handle simple servos to controll a rotatable turret (or somthing else).
    Copyright (C) 2023  br-mat

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import json

class ServoController:
    def __init__(self, servo_pin: int, direction: str):
        # Initialize GPIO and servo motor
        self.factory = PiGPIOFactory()
        self.servo = Servo(servo_pin, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory)
        
        # Store the direction and position
        self.dir = direction.lower()[:10]
        self.position_file = '/home/youruser/pantiltcamera/src/position.json'
        self.position = self.load_position()

    def validate_position(data):
        # Define the expected keys for the data dictionary
        expected_keys = {"horizontal", "vertical"}
        
        # Check if the keys in the data dictionary match the expected keys
        if set(data.keys()) != expected_keys:
            return False
        
        # Iterate over each key-value pair in the data dictionary
        for value in data.items():
            # Check if the value is an integer and if it's within the range [0, 180]
            if not isinstance(value, int):
                return False
        
        # If all checks passed, return True
        return True

    def move(self, angle: int):
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
                position = json.load(f)[self.dir]
                # Validate the loaded position data
                if not self.validate_position(position):
                    raise ValueError(f"Invalid position data: {position}")
                return position
        except FileNotFoundError:
            return 0
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON in {self.position_file}: {e}")
    
    def save_position(self):
        # Load the position from the file for all directions
        try:
            with open(self.position_file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        # Update the position for the given direction
        if self.dir in data:
            data[self.dir] = self.position

            # Save the position to the file for all directions
            with open(self.position_file, 'w') as f:
                json.dump(data, f)
            
    def down(self, degree):
        # Move the servo down by increasing the position by 15
        try:
            degree_int = int(degree)
        except ValueError:
            raise ValueError("Invalid turn angle. Please provide a number.")
        degree_int = max(min(degree_int, 180), 0)
        self.position += degree_int
        self.move(self.position)

    def down(self, degree):
        # Move the servo down by increasing the position by 15
        try:
            degree_int = int(degree)
        except ValueError:
            raise ValueError("Invalid turn angle. Please provide a number.")
        degree_int = max(min(degree_int, 180), 0)
        self.position += degree_int
        self.move(self.position)

    def cleanup(self):
        # Stop the servo motor and clean up GPIO pins
        self.servo.detach()
        self.factory.close()
