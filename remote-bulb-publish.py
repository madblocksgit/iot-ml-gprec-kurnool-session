# User (Google Colab) - Publisher (Sender) 
# Broker - broker.hivemq.com (Server)
# Bulb (Arduino) - Subscriber (Receiver)

import paho.mqtt.client as mqtt

# create a client object
client=mqtt.Client()

# connect with broker

while True:
  client.connect('broker.hivemq.com',1883)
  print ('Broker Connected')
  print('Enter on to switch on the device')
  print('Enter off to switch off the device')
  k=input('Enter choice: ')
  if(k=="on"):
    print('Device On')
    client.publish('iot/gprec','on')
  elif(k=='off'):
    print('Device Off')
    client.publish('iot/gprec','off')
