sandwich_orders = ['Bread butter','Pastrami','Chicken sandwich','Pastrami','Pastrami','Meatball marinara','Tuna sandwich']
finished_sandwiches =[]

while 'Pastrami' in sandwich_orders:
    print("Pastrami is out of stock")
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_order= sandwich_orders.pop()
    print(f"Making {current_order}")
    finished_sandwiches.append(current_order)

print(finished_sandwiches)
print("\nThe following orders have been prepared:")
for sandwich in finished_sandwiches:
    print(sandwich.title())

