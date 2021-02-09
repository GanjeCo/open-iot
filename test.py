import time

from components.Topic import Topic
from components.Thing import Thing
from components.Device import Device

def printer1(client, userdata, message):
    print("printer1")

def printer2(client, userdata, message):
    print("printer2")

device = Device("Ganjine")

device.add_thing('thing-name')

device.things['thing-name'].add_connection(
    Topic(device.clients['mqtt'], 'salam', printer1, 'topic-name', qos=2, initial_subscribe=True),
    Topic(device.clients['mqtt'], 'aleyk', printer2, 'topic-name2', qos=2, initial_subscribe=True)
)


device.clients['mqtt'].loop_forever()
# print(topic)