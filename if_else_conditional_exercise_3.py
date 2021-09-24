#list_username = ["Vikram", "Shalini", "admin", "Julu", "Tulu"]
list_username =[]

if list_username:
    for username in list_username:
        if username == "admin":
            print(f"Hello {username} would you like a status update?")
        else:
            print(f"Hello {username}, welcome to our website")
else:
    print("Empty list")
