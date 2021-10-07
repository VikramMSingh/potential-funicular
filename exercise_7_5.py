user_input=input("Enter your age")
age = int(user_input)
active = True 

while active:
    if age < 3:
        active = False
        print(f"Since you're {age} years old, entry is free for you")
        break   
    elif age > 3 and age <=12:
        print(f"Since your age is {age}, the price of the ticket is $10")
        break
    else:
        print(f"Since your age is {age}, the price of the ticket is $15")
        break
