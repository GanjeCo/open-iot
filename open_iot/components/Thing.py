from .Topic import Topic
from .Connection import Connection


class Thing():

    def __init__(self, name, device):
        self.name = name
        self.connections = {}
        self.device = device

    def remove_connection(self, connection_to_remove):
        for connection in self.connections:
            if connection.name == connection_to_remove:
                #TODO: remove the event
                del connection

    def add_connection(self, *args):
        for connenction in args:
            if isinstance(connenction, Connection):
                self.connections[connenction.name] = connenction
                print(f'connection {connenction} added to thing {self.name}')
            else:
                raise Exception("connections must be instance of Connection class")
