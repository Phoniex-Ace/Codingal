class dad:

    def __init__(self,eyes,aggresive):
        self.eyes = eyes
        self.aggresive = aggresive
    def display(self):
        print("Your Eye Colour Is:",self.eyes)
        print("You Are Aggresive:",self.aggresive)

class son(dad):

    def __init__(self, eyes, aggresive, name , age):
        self.name = name
        self.age = age
        dad.__init__(self , eyes , aggresive)

obj = son("Penguin",8,"blue",True)
obj.display()