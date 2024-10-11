class veichels:

    def __init__(Veichle_type):
        print('Veichle Is A:',Veichle_type)

class car(veichels):

    def __init__(self):
        veichels.__init__('Car')

print(issubclass(car , veichels))