import serial
import time

# Establish serial connection
ser = serial.Serial('/dev/ttyACM0', 9600)  # Use your Arduino's serial port

while True:
    if ser.in_waiting > 0:
        arduino_data = ser.readline().decode('ascii').strip()
        moisture_value = int(arduino_data)

        # Determine wet or dry based on threshold (adjust as per your sensor)
        if moisture_value > 500:  # Adjust threshold according to your sensor
            print("Soil is dry")
        else:
            print("Soil is wet")

    time.sleep(1)  # Delay for 1 second

# Close the serial connection
ser.close()
