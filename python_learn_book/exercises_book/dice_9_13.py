from random import randint

class Die:
    def __init__(self,sides=6):
        """Initializing the die"""
        self.sides = sides
    
    def roll_dice(self):    
        """Method to roll the dice"""
        side = randint(1,self.sides)
        #print(f"{side}")
        return side

