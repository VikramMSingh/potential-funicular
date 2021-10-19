class Vehicle:
    """Initialize vehicle class"""
    def __init__(self, name, max_speed, mileage, capacity, color="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color 
        self.capacity = capacity 

    def describe_vehicle(self):
        print(f"Color: {self.color.title()} Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")
    
    def fare(self):
        """Calculate fare"""
        self.fare = self.capacity * 100
        print(f"Fare is {self.fare}")
        
class Bus(Vehicle):
    
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage, capacity)
        
    def fare(self):
        """Calculate fare for bus"""
        self.fare = ((self.capacity * 100) + (self.capacity*100)/10)
        print(f"Fare for bus is {self.fare}")
my_vehicle = Bus("School Volvo", 180, 12, 50)
my_vehicle.describe_vehicle()
my_vehicle.fare()

my_vehicle_2 = Vehicle("Audi Q5", 280, 24, 5)
my_vehicle_2.describe_vehicle()
my_vehicle_2.fare()

print(type(my_vehicle)) #Built in function

print(isinstance(my_vehicle, Vehicle)) #Built in function
