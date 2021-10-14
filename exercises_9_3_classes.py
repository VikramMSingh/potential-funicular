class User:
    """Describe user"""
    def __init__(self, first_name, second_name, email):
        """Initialize the user"""
        self.first_name = first_name
        self.last_name = second_name 
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        """Describe the user"""
        print(f"User's name is {self.first_name.title()} {self.last_name.title()} and email is {self.email}")

    def greet_user(self):
        """Greet the user"""
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}")

    def count_login_attempts(self):
        """Count the number of login attempts"""
        print(f"This is your {self.login_attempts} attempt")

    def increment_login_attempt(self):
        """Increment the attempt on a login"""
        self.login_attempts += 1
    
    def reset_login_attempt(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0
        print(f"Login attempt reset to {self.login_attempts}")

class Privileges():
    """Define admin privileges"""
    def __init__(self, privileges=["Ban a user", "Unlock a user"]):        
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin privileges are {self.privileges}")

class Admin(User):
    """Define admin user privileges"""
    def __init__(self, first_name, second_name, email):
        super().__init__(first_name, second_name, email)
        self.privileges = Privileges()
      #  self.privileges = []
#    def add_privileges(self, actions):
 #       """Add privileges"""
  #      self.actions = actions
   #     self.privileges.append(self.actions)
    
   # def show_privileges(self):      
    #    """Show admin priviliges"""
     #   print(f"Admin priviliges are {self.privileges}")
                
