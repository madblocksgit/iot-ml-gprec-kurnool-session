/*
  Target: Publish this data to Google Colab for ML Example
  Input: DHT11 Sensor
  Output: Python Script
*/
#include "DHT.h"

DHT dht(2,DHT11);
void setup() {
  dht.begin();
  Serial.begin(9600);
}

void loop() {
  float hum=dht.readHumidity();
  float temp=dht.readTemperature();
  
  Serial.print("#"); // Start of Format
  Serial.print(","); // Seperator
  Serial.print(hum); 
  Serial.print(","); // Seperator
  Serial.print(temp);
  Serial.println('~'); // End of Format
  delay(2000); // 2seconds of delay
}
