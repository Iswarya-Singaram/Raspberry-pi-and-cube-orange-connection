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





