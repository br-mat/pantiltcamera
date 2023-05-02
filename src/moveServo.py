"""
    This code should make use ot the ServoControllerClass to implement a rotating camera turret with motion eye (or somthing else).
    Copyright (C) 2023  br-mat
    
    Function description:
    This script is used to move a camera's servo motor incrementally by a specified degree in either an up or down direction.
    You need a position file in JSON format that contains angle data for the horizontal and/or vertical servo positions.
    Useing ServoControllerClass to control the servo and reads the servo's current position from a position file in JSON format.
    Provide command line arguments (2 needed 1 optional): the GPIO pin number for the servo, the direction ('up' or 'down'), and the degree of movement (default 20).
    The script then moves the servos incrementally based on the specified degree value, if no angle is passed it will move a default value.
    The direction of movement is determined by the method used.


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

#!/usr/bin/env python
import sys
from ServoControllerClass import ServoController

if __name__ == '__main__':
    # Check that at least two arguments are passed
    if len(sys.argv) < 3:
        raise ValueError("Usage: python vertical_up.py PIN MODE [DEGREE]")

    # Parse the command line arguments
    pin = int(sys.argv[1])
    mode = sys.argv[2]
    degree = int(sys.argv[3]) if len(sys.argv) > 3 else 20

    # Define the dictionary of valid pins and their corresponding directions
    # HINT: Class will validate keys in the position file to match 'horizontal or 'vertical'
    valid_direction = {12: 'horizontal', 13: 'vertical'}

    # Check that the pin argument is in the valid_direction dictionary
    if pin not in valid_direction:
        raise ValueError(f"Error: PIN must be one of {list(valid_direction.keys())}")

    # Check that the mode argument is either 'up' or 'down'
    if mode not in ['up', 'down']:
        raise ValueError("Error: MODE must be either 'up' or 'down'")

    # Check that the degree argument is between 0 and 360
    if not (0 <= degree < 360):
        raise ValueError("Error: DEGREE must be between 0 and 360")

    # Create a servo controller instance for the specified pin and direction
    controller = ServoController(pin, valid_direction[pin], '/home/youruser/pantiltcamera/src/position.json')

    # Move the servo up or down based on the mode argument
    if mode == 'up':
        # Move the servo up by increasing the position by degree
        controller.move(degree)
    else:
        # Move the servo down by decreasing the position by degree
        controller.move(degree*-1)

    # Clean up GPIO pins
    controller.cleanup()

    # Exit the program
    raise SystemExit