from dice_9_13 import *

die_1 = Die()

result = []
for roll_num in range(10):
    roll = die_1.roll_dice()
    result.append(roll)
    
print(f"The result of 10 rolls is : {result}")

die_2 = Die(10)
result_2=[]
for roll_num_2 in range(20):
    roll = die_2.roll_dice()
    result_2.append(roll)

print(f"The result of 20 rolls of a 10 sided dice: {result_2}")

