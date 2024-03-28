places_to_visit=[]

places_to_visit.append("Amsterdam")
places_to_visit.insert(1, "Paris")
places_to_visit.insert(0, "Manchester")
places_to_visit.append("Alaska")
places_to_visit.insert(2, "Grand Canyon")

print(sorted(places_to_visit))
print(places_to_visit)

print(sorted(places_to_visit, reverse=True))

places_to_visit.reverse()
print(places_to_visit)

places_to_visit.reverse()
print(places_to_visit)

places_to_visit.sort()
print(places_to_visit)

places_to_visit.sort(reverse=True)
print(f"These are the places I want to visit {places_to_visit}")
