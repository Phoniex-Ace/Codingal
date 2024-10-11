class bird:

    def __init__(self):
        print("Bird Is Ready")
    def swin(self):
        print('Swim Faster')

class penguin(bird):

    def __init__(self):
        super().__init__()
        print("Penguin Is Ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run Faster")

peggy = penguin()
peggy.whoisThis()
peggy.swin()
peggy.run()