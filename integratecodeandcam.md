Here I’ll give an overview on how to install all packages to operate the servos with Action buttons from motionEye and how to enable the camera.

-----------

## Enable Camera

to enable cam:

    raspi-config

-> interface -> enable cam -> finish & reboot

-----

## prepare packages

prepare servo packages (run this line by line!!!): <br>

    sudo su
    
    apt-get install python3-pip

    apt-get install python3-rpi.gpio pigpio python-pigpio python3-pigpio

    pip3 install gpiozero

if you want to start the gpio deamon manually: 'sudo pigpiod' <br>

make sure pigpio autostart on every boot:

    systemctl start pigpiod

    systemctl enable pigpiod

-----------------------
## copy repo and deploy files at correct locations

copy the repo content into home folder of your user(/home/yourUSER/)

and set permissions

    chmod +rw positions.json

now copy all needed files to your configuration directory (usually: /etc/motioneye/) <br>
relevant files are: left_n, right_n, up_n, down_n, ServoControllerClass.py and moveServo.py

    cp /home/yourUser/pantiltcamera/src/filename /etc/motioneye/filename

and make them executable for all users (keep an eye on permissions as you not want to let some door wide open)

    chmod a+x filename (don’t forget class file)
