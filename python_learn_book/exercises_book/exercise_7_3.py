user_inp = input("Enter a number of your choice")

num = int(user_inp)

if num % 10 == 0: 
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of 10")


