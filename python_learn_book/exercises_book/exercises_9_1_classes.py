class Restaurant:
    """Describe a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant's cuisine"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food")
    
    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"{self.restaunrant_name} serving {self.cuisine_type} is now open!")
    
    def set_number_served(self):
        """Customers served"""
        print(f"Current number of customers served are {self.number_served}")

    def update_number_served(self,customers):
        """Update customers served 
            Reject if they are reducing customers served"""
        if customers >= self.number_served:
            print(f"Updating total served today")
            self.number_served = customers 
        else:   
            print(f"You cannot reduce the total number of customers served today")

    def increment_number_served(self, new_customers):   
        """Increment total number of customers served"""
        self.number_served += new_customers
        print(f"On adding {new_customers} total customers served are {self.number_served}")

class IceCreamStand(Restaurant):
    """Defining Ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        
    def ice_cream_flavors(self,flavor):
        """Which flavor is available"""
        self.flavor = flavor
        print(f"{self.flavor.title()} flavor ice cream available")

