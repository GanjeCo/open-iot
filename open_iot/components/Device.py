from .Thing import Thing
from .Topic import Topic

import paho.mqtt.client as mqtt


class Device():
    
    def __init__(self, name, ID, hostname):
        self.ID = ID
        self.name = name
        self._hostname = hostname
        self.things = {}
        self.clients = {}

        self.create_mqtt_client()

        # fetch_settings()
        self.settings = [
            {'event_name':'lock1', 'event_function':'my_function', 'event_args':'', 'category': 'ganjine', 'direction': 'from_server'},
            {'event_name':'lock2', 'event_function':'my_function', 'event_args':'', 'category': 'ganjine', 'direction': 'from_server'}
        ]

        # create connections
        self.bootstrap_connections()

    def _on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def add_thing(self, thing_name_to_add):
        self.things[thing_name_to_add] = Thing(thing_name_to_add, self)
        print(f'thing {thing_name_to_add} added to device {self.name}')
        return self.things[thing_name_to_add]

    def remove_thing(self, thing_name_to_remove):
        pass

    def create_mqtt_client(self):
        self.clients['mqtt'] = mqtt.Client()

        self.clients['mqtt'].on_log = self._on_log

        self.clients['mqtt'].connect(self._hostname)

    def fetch_settings(self):
        # fetch settings from server
        pass

    def my_function(self, client, userdata, message):
        print('hello', message.payload)
    
    def bootstrap_connections(self):
        for thing in self.settings:
            print(thing['event_name'])

            self.add_thing("{0}_{1}".format(self.ID, thing['event_name']))\
                .add_connection(
                    Topic(
                        self.clients['mqtt'],
                        '{0}/{1}/{2}/{3}'.format(thing['direction'], thing['category'], self.ID, thing['event_name']),
                        eval('self.' + thing['event_function']),
                        'topic-name',
                        qos=2
                    )
                )

            # for event in thing['events']:
            #     self.add_thing('{0}_{1}_{2}'.format(self.ID, thing['pin'], event[0]))\
            #         .add_connection(
            #             Topic(
            #                 self.clients['mqtt'],
            #                 'from_server/ganjine/{0}/{1}'.format(self.ID, event[0], , ),
            #                 eval('self.'+ event[1]),
            #                 'topic-name',
            #                 qos=2
            #         )
            #     )
            # print('thing', thing['pin'])
            # print(self.things)

