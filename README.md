# Soil Moisture Detection using Arduino and Python

This repository contains the code and instructions to detect soil moisture using an Arduino board and Python. The Arduino reads soil moisture levels from a sensor and sends the data over serial communication to Python. Python then interprets this data to determine whether the soil is wet or dry based on a predefined threshold.

## Components Required
- Arduino board (e.g., Arduino Uno)
- Soil moisture sensor (e.g., FC-28)
- USB cable for Arduino
- Computer with Python installed

## Setup Instructions

### Arduino Setup
1. Connect the soil moisture sensor to the Arduino board as follows:
   - VCC pin of the sensor to 5V pin on Arduino
   - GND pin of the sensor to GND pin on Arduino
   - Analog output pin of the sensor to A0 (analog input) pin on Arduino

2. Upload the Arduino code (`moisture_sensor.ino`) provided in this repository to your Arduino board using the Arduino IDE.

### Python Setup
1. Install the required Python libraries using pip: pip install pyserial

2. Open the Python script (`soil_moisture.py`) provided in this repository and update the serial port:
```python
ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/ttyACM0' with your Arduino's serial port







3. Adjust the threshold value in the Python script (soil_moisture.py) based on your sensor readings and environmental conditions:

if moisture_value > 500:  # Adjust threshold according to your sensor
    print("Soil is dry")
else:
    print("Soil is wet")
