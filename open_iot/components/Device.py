from .Thing import Thing

import paho.mqtt.client as mqtt


class Device():
    
    def __init__(self, name, direction, category, ID, hostname):
        self.direction = direction
        self.category = category
        self.ID = ID
        self.name = name
        self._hostname = hostname
        self.things = {}
        self.clients = {}
        
        self.clients['mqtt'] = mqtt.Client()

        self.clients['mqtt'].on_log = self._on_log

        self.clients['mqtt'].connect(self._hostname)

        # self.clients['mqtt'].loop_forever()

    def _on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def add_thing(self, thing_name_to_add):
        self.things[thing_name_to_add] = Thing(thing_name_to_add, self)
        print(f'thing {thing_name_to_add} added to device {self.name}')
        return self.things[thing_name_to_add]

    def remove_thing(self, thing_name_to_remove):
        pass