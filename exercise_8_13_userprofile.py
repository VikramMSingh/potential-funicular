def build_profile(first_name, last_name, **user_profile):
    """Build user profile and store info to dictionary"""
    user_profile['first']=first_name
    user_profile['last']=last_name
    return user_profile

a = build_profile("Vikram", "Singh", location="Cleveland", age = 29)
print(f"{a}")
