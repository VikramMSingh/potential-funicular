cur_users = ["Red", "Blue", "Haaland", "Mbappe", "Koeman"]
a=map(lambda x: x.lower(), cur_users)
b=map(lambda x: x.upper(), cur_users)
cur_lower = list(a)
cur_upper = list(b)
new_users = ["Grey", "Ronaldo", "Julu", "HAALAND", "koeman"]

for new_user in new_users:
    if new_user in cur_users:
        print(f"User {new_user} exists")
    elif new_user in cur_lower:
        print(f"User {new_user} exists")
    elif new_user in cur_upper:
        print(f"User {new_user} exists")
    else:
        print(f"{new_user} is available")


