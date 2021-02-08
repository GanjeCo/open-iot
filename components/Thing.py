
from .Topic import Topic
from .Connection import Connection

class Thing():

    def __init__(self, name):
        self.name = name
        self.connections = []

    def remove_connection(self, connection_to_remove):
        for connection in self.connections:
            if connection.name == connection_to_remove:
                #TODO: remove the event
                del connection

    def add_connection(self, connection_to_add):
        if issubclass(connection_to_add, Connection):
            self.connections.append(connection_to_add)
        else:
            raise Exception('connection must be instace of Topic')
