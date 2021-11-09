# note.py *** a data class ***
# isolates note information and privatizes the note creation time data.
import datetime
import os


class Note:
    def __init__(self, data, priority, tag):
        self.done = False
        self.data = data
        self.day_time = datetime.datetime.now() - datetime.timedelta(hours=4)
        self.priority = priority
        self.tag = tag
    

    def get_data(self):
        return self.data


    def set_data(self, data):
        self.data = data


    def get_status(self):
        return self.done


    def set_status(self, completed):
        print(completed)
        self.done = completed


    def get_priority(self):
        if self.priority is None:
            return "Low"
        else:
            return self.priority


    def set_priority(self, level):
        self.priority = level


    def get_tag(self):
        if self.tag is None:
            return 
        else:
            return self.tag


    def set_tag(self, tag):
        self.priority = tag


    def get_time(self):
        return self.day_time.strftime("%B %d, %Y %I:%M:%S %p")
