prompt = "\nEnter pizza topping:"
prompt += "\n(Enter 'quit' when you are finished)"
topping_list=[]
active = True
while active:
    message= input(prompt)

    if message == 'quit':
        active = False
    else:
        topping_list.append(message)
        print(f"We will add {message} to the pizza")
        print(topping_list)
