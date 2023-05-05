Thanks to the documentation of motionEye it is a really simple setup process to make motionEye run on your system. For the original information click:
- [Bullseye](https://github.com/motioneye-project/motioneye/wiki/Install-on-Raspbian-Bullseye)
- [Buster](https://github.com/motioneye-project/motioneye/wiki/Install-On-Raspbian)

I will add the steps I followed below and add additional basic ones to setup your OS on the RaspPi. I tested this with Buster on Raspberry Pi Zero W and Zero 2 W:
<br>

------------------------------------
First we need to get the Raspberry Image on the SD card. For that you can use the [RaspberryPi Imager](https://www.raspberrypi.com/software/).

<br>

Then select the OS like shown below. You can try others as well but make sure to use the latest guide from motionEye to complete the installation.

![Picture 1: bake OS](/doc/imager.jpg "bake OS")

Reinsert your SD card and create a file on the card called 'wpa_supplicant.conf', this file should give you access to your local Network:

    country=yourCOUTRYCODE
    update_config=1
    ctrl_interface=/var/run/wpa_supplicant

    network={
     scan_ssid=1
     ssid="yourSSID"
     psk="yourPassword"
    }

Now plug your SD-card into the Pi and power it.

-------------------------------------
Make things easy

    sudo su

now change your password (IMPORTANT!) and remember it (Optional?)

    passwd root
    
by default on most Pi's the command 'sudo su' wont ask for password, let's change that

    sudo visudo /etc/sudoers.d/010_pi-nopasswd
    
now you should be able to see the line: 'pi ALL=(ALL) NOPASSWD: ALL' <br>
change it to:

    pi ALL=(ALL) ALL

then update your system

    apt-get update && apt-get upgrade -y

install a bunch of packages (execute ALL following code line by line!!!)

    apt-get install ffmpeg libmariadb3 libpq5 libmicrohttpd12 -y
    
    wget https://github.com/Motion-Project/motion/releases/download/release-4.3.2/pi_buster_motion_4.3.2-1_armhf.deb

    dpkg -i pi_buster_motion_4.3.2-1_armhf.deb

    apt-get install python-pip python-dev libssl-dev libcurl4-openssl-dev libjpeg-dev libz-dev -y

Hint: if you run into an issue with pill --> (if pill hang at 99% run the following: 'apt-get install python-pil -y' and then again 'pip install motioneye')

    pip install motioneye

create the config directory

    mkdir -p /etc/motioneye

    cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf

    mkdir -p /var/lib/motioneye

    cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service

let it autostart on boot

    systemctl daemon-reload

    systemctl enable motioneye

    systemctl start motioneye

----------------------

This should do the job. Now find out the IP of your device. You can now visit on your web browser:

    your.rasp.pi.IP:8765

Now you should be able to see the motionEye page.

