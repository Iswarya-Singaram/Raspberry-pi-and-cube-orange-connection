# Raspberry-pi-and-cube-orange-connection


## Raspberry Pi to Cube FC UART Setup

This repository provides scripts and instructions to configure a Raspberry Pi to communicate with Cube Orange/Black flight controllers via UART.

## Setup Steps

### 1. Connect Hardware
Wire the Raspberry Pi's UART pins to the Cube FC according to the provided diagram.

<p align=center>
<img src="https://github.com/user-attachments/assets/7fb85866-6169-4e99-9c1a-69512b59a338" height="300">
</p>


### 2. Configure Raspberry Pi Serial Port
Run the following command to disable the serial console and enable UART:
```bash
sudo raspi-config
```
Navigate to **Interface Options** → **Serial Port**.
- Disable the login shell over serial (**No**).
- Enable the serial port hardware (**Yes**).

Reboot the Raspberry Pi:
```bash
sudo reboot
```

### 3. Disable Bluetooth (To Free Up UART)
Edit the config file:
```bash
sudo nano /boot/firmware/config.txt
```
Add the following line at the bottom:
```ini
dtoverlay=disable-bt
```
Save and exit, then reboot:
```bash
sudo reboot
```
To check if the blutooth has been disabled and the UART is free try,
~~~
ls /dev/ttyAMA0
~~~

### 4. Set Up Python Environment
Install Python 3.8 and create a virtual environment:
```bash
sudo apt update
sudo apt install python3.8 python3.8-venv python3.8-dev -y
python3.8 -m venv drone
source drone/bin/activate
```

### 5. Install Required Packages
Dronekit 2.9.2
Mavproxy 1.8.46
PyMavlink 2.4.8

### 6. Accessing Mavproxy
MAVproxy can be accessed via the following command

```
mavproxy.py --master=/dev/ttyAMA0 --baudrate=921600
```

Note: Adjust the baurate according to your requirements

### 7. To check for heartbeat run the following code

```
from pymavlink import mavutil

master = mavutil.mavlink_connection('/dev/ttyAMA0',baud=57600)

print("waiting for heartbeat...")

master.wait_heartbeat()
print(f"{master.target_system}")

```
Note: If you cannot receive the heartbeat. Adjust the baudrate to 9600,57600,115200, 921600..etc.. until we know in which baudrate pi and FC are communicating.



