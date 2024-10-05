class fruit:
    taste = 'sweet'
    def __init__(self,name,colour):
        self.name = name
        self.color = colour

apple = fruit('Apple','Red')
banana = fruit('Banana','Yellow')

print(apple.taste)
print(banana.name, apple.color)
print(banana.name, banana.color)