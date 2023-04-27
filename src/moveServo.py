"""
    This code should make use ot the ServoControllerClass to implement a rotating camera turret with motion eye (or somthing else).
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
    degree = int(sys.argv[3]) if len(sys.argv) > 3 else 10

    # Define the dictionary of valid pins and their corresponding directions
    valid_pins = {12: 'horizontal', 13: 'vertical'}

    # Check that the pin argument is in the valid_pins dictionary
    if pin not in valid_pins:
        raise ValueError(f"Error: PIN must be one of {list(valid_pins.keys())}")

    # Check that the mode argument is either 'up' or 'down'
    if mode not in ['up', 'down']:
        raise ValueError("Error: MODE must be either 'up' or 'down'")

    # Check that the degree argument is between 0 and 360
    if not (0 <= degree < 360):
        raise ValueError("Error: DEGREE must be between 0 and 360")

    # Create a servo controller instance for the specified pin and direction
    controller = ServoController(pin, valid_pins[pin])

    # Move the servo up or down based on the mode argument
    if mode == 'up':
        # Move the servo up by decreasing the position by degree
        controller.up(degree)
    elif mode == 'down':
        # Move the servo down by increasing the position by degree
        controller.down(degree)

    # Clean up GPIO pins
    controller.cleanup()

    # Exit the program
    raise SystemExit