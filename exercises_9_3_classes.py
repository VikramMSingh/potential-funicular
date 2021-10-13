class User:
    """Describe user"""
    def __init__(self, first_name, second_name, email):
        """Initialize the user"""
        self.first_name = first_name
        self.last_name = second_name 
        self.email = email
    
    def describe_user(self):
        """Describe the user"""
        print(f"User's name is {self.first_name.title()} {self.last_name.title()} and email is {self.email}")

    def greet_user(self):
        """Greet the user"""
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}")


    
