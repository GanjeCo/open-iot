
import paho.mqtt.client as mqtt

from .Connection import Connection
class Topic(Connection):
    '''
    A wrapper on paho.mqtt protocol  
    '''
    def __init__(self, client, topic, name='', sub_event=None, initial_subscribe=False, qos=0):
        '''
        constructor
        '''
        self.client = client 
        self.topic = topic
        self.name = name
        self.qos = qos
        self._is_sub = False

        if sub_event != None and callable(sub_event):
            self.assign_sub_funtion(sub_event)

        if initial_subscribe == True:
            self.do_subscribe()
        
    def do_subscribe(self):
        '''
        do subscribe
        '''
        self.client.subscribe(self.topic, qos=self.qos)
        self._is_sub = True
        return True

    def do_unsubscribe(self):
        '''
        do unsubscribe
        '''
        self.client.unsubscribe(self.topic)
        self._is_sub = False
        return False

    def is_subscribe(self):
        '''
        returns True if is subscribed to the topic 
        '''
        return self._is_sub

    def publish(self, payload, qos=0):
        '''
        publish payload to the topic with given qos
        payload must be str
        '''
        self.client.publish(self.topic, payload=payload, qos=qos)

    def assign_sub_funtion(self, subscribe_event):
        '''
        assign subscribe_event to the Topic 
        if  subscribe_event == None will unassign all events on topic
        '''
        if subscribe_event == None:
            self.assign_unsub_function()
        elif callable(subscribe_event):
            self._subscribe_event = subscribe_event
            self.client.message_callback_add(self.topic, self._subscribe_event)
        else:
            raise Exception('subscribe_event must be callable or None')

    def assign_unsub_function(self):
        '''
        un assign all callbacks from the Topic
        '''
        self.client.message_callback_remove(self.topic)

    def make_payload(self):
        '''
        can be used to produce the payload for the Topic
        '''
        raise NotImplementedError("This method is not Implemented!")

    def _sub_event(self, client, userdata, message):
        '''
        the actual event to be called if function is assigned to the Topic
        '''
        raise NotImplementedError("This method is not Implemented!")

    def __str__(self):
        '''
        overwrite the to string method
        '''
        return str({"name": self.name, "topic":self.topic})
