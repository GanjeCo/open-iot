import time

from open_iot.components.Topic import Topic
from open_iot.components.Thing import Thing
from open_iot.components.Device import Device


def printer1(client, userdata, message):
    print("printer1")

def printer2(client, userdata, message):
    print("printer2")

device = Device("Ganjine", "5.253.26.31")

device.add_thing('sensor1').add_connection(
    Topic(device.clients['mqtt'], 'salam', printer1, 'topic-name', qos=2)
    )

device.add_thing('sensor2').add_connection(
    Topic(device.clients['mqtt'], 'asd/salam/#', printer2, 'topic2-name', qos=2)
    )


device.clients['mqtt'].loop_forever()
# print(topic)