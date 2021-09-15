'''insert - to insert at a particular position in a list. append - add at the end of the list. pop - to remove the last element & pop[1] to remove a element at position 1 of ths list. del - del[x] or del["x"] to remove something from list at a particular position. remove['Barack Obama'] - to remove the first element that matches Barack Obama from the list '''

guest_list = []

guest_list.append("Jeff Bezos")
guest_list.append("Elon Musk")
guest_list.append("Mahatma Gandhi")

not_coming = guest_list.pop(2)

print(f"Due to unforeseen circumstances {not_coming} cannot make it to the dinner")

guest_list.insert(0,"Sir Alex Ferguson")

print("Hello, \n \t Since we have booked a large table we are inviting more people to the exclusive dinner")
guest_list.insert(1,"Ratan Tata")
guest_list.insert(2,"Dr.Manmohan Singh")
guest_list.append("Barack Obama")
for guests in guest_list:
	print(f"Dear {guests}, \n \t You are cordially invited to the dinner party")

uninvited_guests=[]
ui_1 = guest_list.pop(2)
ui_2 = guest_list.pop(3)
ui_3 = guest_list.pop()
ui_4 = guest_list.pop()
uninvited_guests.append(ui_1)
uninvited_guests.insert(1, ui_2)
uninvited_guests.append(ui_3)
uninvited_guests.append(ui_4)

for ug in uninvited_guests:
	print(f"Dear {ug}, \n \t Due to delayed delivery of the table by Amazon, we will fail to accomodate you, so we are rescinding our invite. Please blame {ui_4}.") 

del guest_list[1]
del guest_list[0]

print(f"Empty list \n \t {guest_list}")
