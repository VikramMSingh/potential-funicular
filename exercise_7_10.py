vacation={}

active = True 

while active:
    name = input("Enter your name")
    vac = input("Your dream city to go to vacation")
    vacation[name]=vac
    
    repeat = input("Do you want others to vote? Yes/No")

    if repeat=="No":
        active = False
        print("Polling has ended")

for name, dest in vacation.items():
    print(vacation)
    print(f"{name}'s favorite destination is {dest}")

