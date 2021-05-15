class Topic():
    '''
    A wrapper on paho.mqtt protocol
    '''
    def __init__(self, device, topic, event, name, qos=0):
        '''
        constructor
        '''
        self.name = name 
        self.device = device 
        self.topic = topic
        self.qos = qos
        self._is_sub = False
        if callable(event):
            self._event = event
            self.assign_subscribe_funtion(self._event)
        else:
            raise Exception("event must be callable function")

        self.do_subscribe()
        
    def do_subscribe(self):
        '''
        do subscribe
        '''
        self.device.client.subscribe(self.topic, qos=self.qos)
        self._is_sub = True
        return True

    def do_unsubscribe(self):
        '''
        do unsubscribe
        '''
        self.device.client.unsubscribe(self.topic)
        self._is_sub = False
        return True

    def is_subscribed(self):
        '''
        returns True if is subscribed to the topic 
        '''
        return self._is_sub

    def publish(self, payload, qos=0):
        '''
        publish payload to the topic with given qos
        payload must be str
        '''
        self.device.client.publish(self.topic, payload=payload, qos=qos)

    def assign_subscribe_funtion(self, subscribe_event):
        '''
        assign subscribe_event to the Topic 
        if  subscribe_event == None will unassign all events on topic
        '''
        if subscribe_event == None:
            self.assign_unsub_function()
        elif callable(subscribe_event):
            self._subscribe_event = subscribe_event
            self.device.client.message_callback_add(self.topic, self._subscribe_event)
        else:
            raise Exception('subscribe_event must be callable or None')

    def assign_unsubscribe_function(self):
        '''
        un assign all callbacks from the Topic
        '''
        self.device.client.message_callback_remove(self.topic)

    def make_payload(self):
        '''
        can be used to produce the payload for the Topic
        '''
        raise NotImplementedError("This method is not Implemented!")

    def __str__(self):
        '''
        overwrite the to string method
        '''
        return str({"name": self.name, "topic":self.topic})

