
class Note:
    def __init__(self, data):
        self.done = False
        self.data = data
    

    def get_data(self):
        return self.data

    
    def get_status(self):
        return self.done

    
    def set_status(self, completed):
        self.done = completed

    def set_data(self, data):
        self.data - data
