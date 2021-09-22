basic_foods = ("butter chicken", "chicken tandoori", "chicken biryani", "garlic naan", "kesar kulfi")

for food in basic_foods:
    print(f"{food}".title())


'''basic_foods.insert[0] = "Elaichi" 
This command will fail'''

basic_foods = ("butter chicken", "chicken tikka", "chicken biryani", "garlic naan", "malai kulfi")

print("Updated menu:")
for food in basic_foods:
    print(f"\t{food}".title())
