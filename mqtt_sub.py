# subscriber
import paho.mqtt.client as mqtt
import time

# create a client object
client=mqtt.Client()

# connect with broker
client.connect('broker.hivemq.com',1883)
print ('Broker Connected')

# subscribe on the topic
client.subscribe('iot/gprec')

def notification(client,userdata,msg):
 print(msg.payload)

client.on_message=notification
client.loop_forever()
