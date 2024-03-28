from timer import *

date = input("Please enter the date you want to calculate from: ")
a = timer(date)
b = a.validate_date()
c = a.calculate_diff()
print(c)


