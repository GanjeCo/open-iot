import json

from .Topic import Topic

import paho.mqtt.client as mqtt

import time

class Device():
    
    def __init__(self, ID, hostname, name='ganjine', is_server=False):
        self.name = name
        self.ID = ID
        self._hostname = hostname
        self.topics = {}
        self.settings = []
        self.is_init = True

        self.create_mqtt_client()

    def create_mqtt_client(self):
        self.client = mqtt.Client(self.name + "_" + self.ID)

        self.client.on_log = self._on_log
        self.client.on_connect = self._on_connect

        self.client.connect(self._hostname)

    def add_topic(self, topic_name, callerback, category, qos=1):
        if topic_name in self.topics.keys():
            return False
        else:
            self.topics[topic_name] = Topic(
                self, 
                '{0}/{1}/{2}/{3}'.format('from_server', self.name, self.ID, category), 
                callerback,
                topic_name,
                qos=qos
                )
            return True

    def remove_topic(self, thing_name_to_remove):
        pass

    def _on_connect(self, client, userdata, flags, rc):
        self.request_settings()

        if not self.is_init:
            for topic in self.topics:
                self.topics[topic].do_subscribe()
                
        self.is_init = False

    def _on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def request_settings(self):
        pass
        # fetch settings from server
        self.add_topic(
            'settings',
            self.set_settings,
            'settings',
        )

        self.publisher('settings')

    def set_settings(self, client, userdata, message):
        self.settings = json.loads(message.payload)

    def publisher(self, topic, payload='', qos=0):
        self.client.publish(
            '{0}/{1}/{2}/{3}'.format('to_server', self.name, self.ID, topic),
            payload=payload, 
            qos=qos
            )

