count_to_twenty=[]
count_to_twenty=[i for i in range(1,21)]
print(count_to_twenty)

count_to_million=[]
count_to_million=[i for i in range(1,1000001)]
#print(count_to_million)
print(min(count_to_million))
print(max(count_to_million))
print(sum(count_to_million))

odd_numbers = []
odd_numbers = [i for i in range(1,20,2)]
for odd in odd_numbers:
	print(odd)

print(f"The first three items in the list are: {odd_numbers[0:3]}")

print(f"Three items from the middle of the list are: {odd_numbers[5:9]}")

print(f"The last three items in the list are: {odd_numbers[-3:]}")
