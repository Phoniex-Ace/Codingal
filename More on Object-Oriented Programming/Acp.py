import math

class Circle:
    # Constructor to initialize the radius
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate the area of the circle
    def area(self):
        return math.pi * self.radius ** 2

    # Method to calculate the perimeter of the circle
    def perimeter(self):
        return 2 * math.pi * self.radius

# Creating an instance of Circle with a specific radius
circle = Circle(5)

# Displaying the area and perimeter
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")
