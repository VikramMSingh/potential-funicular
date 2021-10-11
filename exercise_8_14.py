def car_details(make, model, **car_info):
    """Return details about a car"""
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = car_details("VW", "Tiguan", color = "black")

#print(car)
print(f"The make is {car['make']}, model is {car['model']}, and color is {car['color']}")

