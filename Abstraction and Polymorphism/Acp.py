class BMW:
    def start(self):
        return "BMW is starting with a smooth engine sound."

    def accelerate(self):
        return "BMW is accelerating to 100 km/h in 5 seconds."

    def stop(self):
        return "BMW is stopping with advanced brakes."

class Ferrari:
    def start(self):
        return "Ferrari roars to life with a powerful engine sound."

    def accelerate(self):
        return "Ferrari accelerates to 100 km/h in just 3 seconds."

    def stop(self):
        return "Ferrari stops with high-performance brakes."

# Polymorphism example
def test_drive(car):
    print(car.start())
    print(car.accelerate())
    print(car.stop())

# Creating instances
bmw_car = BMW()
ferrari_car = Ferrari()

# Test driving each car
print("BMW Test Drive:")
test_drive(bmw_car)
print("\nFerrari Test Drive:")
test_drive(ferrari_car)
