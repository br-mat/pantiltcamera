#!/usr/bin/env python

from servo_controller import ServoController

if __name__ == '__main__':
    # Create a servo controller instance for left direction and pin 1
    controller = ServoController(12, 'horizontal')

    # Move the servo up by decreasing the position by 10
    controller.up()

    # Clean up GPIO pins
    controller.cleanup()

    # Exit the program
    raise SystemExit