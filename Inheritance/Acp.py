class Vehicle:
    def __init__(self, num_passengers, fare_per_passenger):
        self.num_passengers = num_passengers
        self.fare_per_passenger = fare_per_passenger

    def calculate_fare(self):
        raise NotImplementedError("Subclasses must implement calculate_fare method")

class Bus(Vehicle):
    def __init__(self, num_passengers, fare_per_passenger, distance_traveled):
        super().__init__(num_passengers, fare_per_passenger)
        self.distance_traveled = distance_traveled

    def calculate_fare(self):
        base_fare = self.num_passengers * self.fare_per_passenger
        distance_surcharge = self.distance_traveled * 0.10 
        total_fare = base_fare + distance_surcharge
        return total_fare

if __name__ == "__main__":
    num_passengers = int(input("Enter the number of passengers: "))
    fare_per_passenger = float(input("Enter the fare per passenger: "))
    distance_traveled = float(input("Enter the distance traveled (in miles): "))

    bus = Bus(num_passengers, fare_per_passenger, distance_traveled)
    total_fare = bus.calculate_fare()
    print("Total fare: ${:.2f}".format(total_fare))