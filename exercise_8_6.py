def city_country(city, country):
    location=f"{city},{country}"
    return location

city_user = input("Enter your favorite cities")
country_user = input("Enter your favorite country")

user_location = city_country(city_user, country_user)

print(user_location)
