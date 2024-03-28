cities = {
    "Mumbai": {
        "country":"India", 
        "population": 100000000, 
        "fact":"Vikram Singh is from here"}, 
    "Cleveland": {
        "country":"USA", 
        "population": 200000, 
        "fact":"Vikram Singh studied here"}, 
    "Manchester":{
        "country":"UK", 
        "population": 250000, 
        "fact": "Manchester United the greatest club is from here"}
}

for city, city_info in cities.items():
    print(f"{city}".title())
    print(f"\tLocated in {city_info['country']}, with a population of {city_info['population']}\n")
    print(f"\t{city} is known because {city_info['fact']}")
