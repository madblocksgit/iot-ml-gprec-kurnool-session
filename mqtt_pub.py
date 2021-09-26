import paho.mqtt.client as mqtt
import time

# create a client object
client=mqtt.Client()

# connect with broker
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

# publish the data
while True:
 client.publish('iot/gprec','Hi Hello from FDP')
 time.sleep(2) # 2 seconds
 
