fav_pizza_toppings = ["pineapple","jalapeno","mushroom","chicken"]

friend_pizza_toppings = fav_pizza_toppings[:]

friend_pizza_toppings.insert(0, "pepperoni")

print("My pizza toppings are:{}".format(fav_pizza_toppings))

print(f"My friend's pizza toppings are{friend_pizza_toppings}")

for toppings in fav_pizza_toppings:
	print(f"My favorite pizza topping is:\n\t {toppings}")
