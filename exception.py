a = input("Enter a value")
b = input("Enter a value")

try:
    num_a = int(a)
    num_b = int(b)
    print(num_a+num_b)
except Exception as e:
    print(f"Error code:{e}")
