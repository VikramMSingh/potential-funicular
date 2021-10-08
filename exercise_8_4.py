def make_shirt(message,size="L"):
    """make shirt of specific size and message"""
    print(f"The size of the shirt is {size}")
    print(f"Message to be printed on the shirt - {message}")

#shirt_size = input("Enter t-shirt size as S - Small, M - Medium, L - Large, XL - Extra Large")

shirt_message = input("Enter message you want to print on your shirt")

make_shirt(shirt_message)
#make_shirt(shirt_message,"M") - to change from default(L) to M
