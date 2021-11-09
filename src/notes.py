class Notes:

    def __init__(self) :
        self.notes = []

    def add (self, note):
        self.notes.append(note)
        return self.notes
    
    def get_all(self):
        return self.notes
    
    def get_size(self) : 
        return len(self.notes)

    def get_one(self, idx):
        return self.notes[idx]
    
    def insert(self, idx, note):
        self.notes.insert(idx, note)

    def remove(self, idx):
        self.notes.pop(idx)