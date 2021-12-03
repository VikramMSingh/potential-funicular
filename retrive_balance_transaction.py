import stripe
import csv
stripe.api_key = "sk_test_51JsfSkEAQrNAOMfHaZN0gmuiygZew7CmMwGiY4KtOKI2hWuSIBj1F448wH1bDkaxUt0Q6nv77k5upHDJ75OqxasP00ruHFIQNA"

output = stripe.BalanceTransaction.list()

#print(output)
#print(output.keys())

output_dict = output['data']

data_file = open('output_file.csv','w')
file_writer = csv.writer(data_file)
count = 0
for i in output_dict:
    print(i)
    if count == 0:
        header = (i)
        file_writer.writerow(header)
        count += 1
    elif count > 0:
        file_writer.writerow(i.values())

data_file.close()

