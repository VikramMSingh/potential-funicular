glossary = {"list":"Data structure to store values", "append":"Add value to the end of the list", "insert":"Add value at a particular position", "sort":"permanently sort a list in ascending order","pop":"remove element from end of the list unless position specified"}

glossary["sorted"] = "Temporarily sort a list or dictionary"
#print(f"{glossary['list']}\n{glossary['append']}\n{glossary['insert']}\n{glossa#ry['sort']}\n{glossary['pop']}")

for key, value in glossary.items():
    print(f"\n{key.title()}:{value.title()}")
