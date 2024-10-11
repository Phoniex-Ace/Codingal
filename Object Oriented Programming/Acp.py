class Dog:
    # Class variable
    species = "Canine"

    # Constructor to initialize instance variables
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Method to display dog details
    def display_details(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")

# Creating instances for two different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Beagle")

# Displaying the details
dog1.display_details()
dog2.display_details()
