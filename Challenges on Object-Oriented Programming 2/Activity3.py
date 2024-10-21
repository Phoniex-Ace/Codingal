class FruitQuiz:

    def __init__(self):
        self.fruits = {'apple': 'red', 'orange' : 'orange' , 'watermelon' : 'green' , 'banana' : 'yellow'} 

    def quiz(self):
        while(True):

         fruit, color= random.choice(list(self.fruits.items()))
         print("What Is The Colour Of: ")