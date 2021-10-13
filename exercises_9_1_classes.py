class Restaurant:
    """Describe a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant's cuisine"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food")
    
    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"{self.restaunrant_name} serving {self.cuisine_type} is now open!")

