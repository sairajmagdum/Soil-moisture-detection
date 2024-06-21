void setup() {
    Serial.begin(9600); // Initialize serial communication
}

void loop() {
    int moistureValue = analogRead(A0); // Read analog input from A0 pin
    Serial.println(moistureValue); // Send the sensor value to serial port
    delay(1000); // Delay for 1 second
}
