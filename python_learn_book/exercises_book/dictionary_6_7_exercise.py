people_1 = {"fname":"Vik", "lname":"Sin", "age":29}
people_2 = {"fname":"Sal", "lname":"Sin", "age":25}
people_3 = {"fname":"Man", "lname":"Wom", "age":18}

people = [people_1, people_2, people_3]

for person in people:
    print(f"Full name is {person['fname']} {person['lname']} and age is {person['age']}")

