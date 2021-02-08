from .Thing import Thing

import paho.mqtt.client as mqtt

class Device():
    
    def __init__(self, *args, **kwargs):
        self._hostname = "5.253.26.31"
        self.things = []

        self.mqtt_client = mqtt.Client()

        self.mqtt_client.on_log = self._on_log

        self.mqtt_client.connect(self._hostname)

        self.mqtt_client.loop_forever()

    def _on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def add_thing(self, thing_to_add):
        if isinstance(thing_to_add, Thing):
            self.things.append(thing_to_add)
        else:
            raise Exception("thing_to_add must be instace of Thing class")

    def remove_thing(self, thing_name_to_remove):
        for thing in self.things:
            if thing.name == thing_name_to_remove:
                #TODO: thing must be stopped working
                del thing
