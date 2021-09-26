# This is the program which collects data from arduino and pushes that data to Google Colab
import serial
import paho.mqtt.client as mqtt

ser=serial.Serial('COM4',9600,timeout=0.5)
client=mqtt.Client()
while True:
 if(ser.inWaiting()>0):
  k=ser.readline()
  print(k)
  client.connect('broker.hivemq.com',1883)
  print ('Broker Connected')
  client.publish('iot/gprec',k)
