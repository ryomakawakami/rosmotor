# rosmotor
Raspberry Pi project with ROS and motors

## Setup

### Initial

Download Raspberry Pi image from Ubiquity Robotics. Write to SD card and load on Pi.
Turn on Pi. Connect to wifi network (ubiquityrobotXXXX, XXXX is first four digits of MAC address). Password ```robotseverywhere```.
Sudo password is ```ubuntu```.
```sudo systemctl disable magni-base``` to disable Ubiquity Robotics scripts.

Set static IP on machines. Write into /etc/hosts on all machines (```C:\Windows\System32\Drivers\etc\hosts``` in Windows). Ping all to ensure connection.
```
raspberrypi 169.254.161.92
ubuntu      169.254.161.100
windows     169.254.161.150
```

Disable firewall ```sudo ufw disable```

### Running roscore on Ubuntu laptop

**Setup .bashrc on Pi**

Remove

```source /etc/ubiquity/env.sh```

Add

```
export ROS_HOSTNAME=raspberrypi
export ROS_MASTER_URI=http://ubuntu:11311
export ROS_IP=169.254.161.92
```

**Setup .bashrc on Ubuntu laptop**

Add

```
export ROS_HOSTNAME=ubuntu
export ROS_MASTER_URI=http://ubuntu:11311
export ROS_IP=169.254.161.100
```

### Test

On ubuntu: ```roscore```

*Verify one direction*

On raspberrypi: ```rosrun rospy_tutorials listener.py```

On ubuntu: ```rosrun rospy_tutorials talker.py```

*Verify other direction*

On raspberrypi: ```rosrun rospy_tutorials listener.py```

On ubuntu: ```rosrun rospy_tutorials talker.py```

If only one direction works, check ```ROS_HOSTNAME``` on both machines.

**Useful commands**

```rostopic list```

```rostopic info [topic]```

```rosnode list```

```rosnode info [node]```

### Camera

Reference http://roboticsweekends.blogspot.com/2017/12/how-to-use-usb-camera-with-ros-on.html

Check if camera is recognized with ```lsusb```

Install ROS node with ```sudo apt install ros-kinetic-usb-cam```

Start ```roscore``` and ```roslaunch usb_cam usb_cam-test.launch```

View image with ```rosrun image_view image_view image:=/usb_cam/image_raw```

### MATLAB

Connect to ubuntu master.

```
setenv('ROS_HOSTNAME', '169.254.161.150')
setenv('ROS_MASTER_URI', 'http://169.254.161.100:11311')
setenv('ROS_IP', '169.254.161.150')
rosinit
```

Disable firewall settings for port in settings (in anti-virus software too).
