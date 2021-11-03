# note.py *** a data class ***
# isolates note information and privatizes the note creation time data.
import datetime


class Note:
    def __init__(self, data, priority, tag):
        self.done = False
        self.data = data
        self.time = datetime.datetime.now()
        self.priority = priority
        self.tag = tag
    

    def get_data(self):
        return self.data


    def set_data(self, data):
        self.data - data


    def get_status(self):
        return self.done


    def set_status(self, completed):
        self.done = completed


    def get_priority(self):
        return self.priority


    def set_priority(self, level):
        self.priority = level


    def get_tag(self):
        return self.tag


    def set_tag(self, tag):
        self.priority = tag


    def get_time(self):
        return f"{self.time.month}/{self.time.day}/{self.time.year} {self.time.hour}:{self.time.minute}:{self.time.second}"
