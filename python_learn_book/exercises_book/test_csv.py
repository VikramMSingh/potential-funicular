import csv

class CSVTEST:
    def __init__(self,row,header):
        self.__dict__ = dict(zip(header,row))

data = list(csv.reader(open('test_api.csv')))

for i in data[1:]:
    instance = CSVTEST(i, data[0])
    print(instance.values())
