

class Connection():
    def __init__(self, name):
        self.name = name

    def _event(self):
        '''
        the actual event to be called if function is assigned to the Connection
        '''
        raise NotImplementedError("This method is not Implemented!")