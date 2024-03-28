from exercises_9_1_classes import Restaurant, IceCreamStand

my_first_restaurant = Restaurant("Image", "North Indian")
my_second_restaurant = Restaurant("Maki", "Japanese")
my_third_restaurant = Restaurant("Athens", "Continental")

my_first_restaurant.describe_restaurant()
my_first_restaurant.update_number_served(100)
my_first_restaurant.set_number_served()
my_first_restaurant.increment_number_served(20)
my_first_restaurant.set_number_served()
my_second_restaurant.describe_restaurant()
my_third_restaurant.describe_restaurant()

my_first_ice_cream_stand = IceCreamStand("Ice Republic", "Ice Cream")
my_first_ice_cream_stand.ice_cream_flavors("Chocolate")
