class Car:
    """Describe a car"""
    def __init__(self, make, model, year, odometer_reading):
        """Initialize the car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
    def describe_car(self):
        """Describe the car"""
        if self.odometer_reading > 0: 
            print(f"We have a used {self.make.title()} {self.model.title()} car from {self.year} with {self.odometer_reading} miles on it")
        else:
            print(f"We have a new {self.make.title()} {self.model.title()} car from {self.year}")

    def update_odometer(self, mileage):
        """Update the odometer"""
        if mileage > self.odometer_reading:     
            self.odometer_reading = mileage
        else:
            print(f"Updated mileage cannot be less than actual mileage {self.odometer_reading}")
    
    def increment_mileage(self, miles):
        """Update odometer if car travels"""
        if miles > 0:
            self.odometer_reading += miles 
        else:
            print(f"Car did not travel")
class Battery:
    """Describe car battery"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Get range based on battery"""
        if self.battery_size > 75:
            range = 400
        elif self.battery_size <= 75:
            range = 260 
        else:
            range = 0
        print(f"This car can go about {range} miles on a full charge")   

class ElectricCar(Car):
    """Describe an electric car"""
    def __init__(self, make, model, year, odometer_reading):
        """Initialize electric car"""
        super().__init__(make, model, year, odometer_reading)
        self.battery = Battery()
   

    def upgrade_battery(self):
        """Upgrade batter size"""
        if self.make == "Tesla":
            self.battery.battery_size = 100
        else:
            self.battery.battery_size = 75

#    def get_range(self, range=0):
#        """Get range based on battery"""
#        self.range = range
#        if self.battery.battery_size > 75:
#            self.range = 400
#        elif self.battery.battery_size <= 75:
#            self.range = 260
#        print(f"This car can go about {range} miles on a full charge")
    
    def describe_car(self):
        """Electric cars have range"""
        print(f"This is the electric car {self.make.title()} {self.model.title()} with a mileage of {self.odometer_reading}, battery of {self.battery.battery_size}-kWH")
