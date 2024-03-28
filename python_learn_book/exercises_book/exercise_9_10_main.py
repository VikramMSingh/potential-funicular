from exercises_9_10_classes import Car, ElectricCar, Battery 

my_car = Car("Volkswagen", "Tiguan" , 2014, 78000)
my_car.describe_car()
my_car.update_odometer(1000)
my_car.increment_mileage(-10)
my_car.increment_mileage(600)
my_car.describe_car()

my_electric_car = ElectricCar("Tesla", "Model S", 2021, 0)
my_electric_car.describe_car()
my_electric_car.upgrade_battery()
my_electric_car.describe_car()
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()

my_electric_car_2 = ElectricCar("Chevy", "Bolt", 2021, 0)
my_electric_car_2.describe_car()
my_electric_car_2.upgrade_battery()
my_electric_car_2.battery.describe_battery()
my_electric_car_2.battery.get_range()
