from .Thing import Thing

import paho.mqtt.client as mqtt

class Device():
    
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self._hostname = "5.253.26.31"
        self.things = {}
        self.clients = {}
        
        self.clients['mqtt'] = mqtt.Client()

        self.clients['mqtt'].on_log = self._on_log

        self.clients['mqtt'].connect(self._hostname)

        # self.clients['mqtt'].loop_forever()

    def _on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def add_thing(self, thing_name_to_add):
        self.things[thing_name_to_add] = Thing(thing_name_to_add, self.clients)
        print(f'thing {thing_name_to_add} added to device {self.name}')

    def remove_thing(self, thing_name_to_remove):
        pass
