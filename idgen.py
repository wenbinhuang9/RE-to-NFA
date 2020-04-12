

class IDGenerator():

    def __init__(self):
        self.count = 0


    def nextID(self):
        id = "q" + str(self.count)

        self.count += 1

        return id