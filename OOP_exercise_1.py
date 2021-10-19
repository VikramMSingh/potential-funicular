class Vehicle:
    """Initialize class vehicle"""
    def __init__(self, max_speed, mileage):
        """Defining vehicle class"""
        self.max_speed = max_speed
        self.mileage = mileage

    def describe_vehicle(self):
        print(f"The vehicle has max speed {self.max_speed} MPH and mileage {self.mileage} miles per gallon")


a = int(input("Enter the max speed"))
b = int(input("Enter the mileage"))

my_car = Vehicle(a,b)
my_car.describe_vehicle()
