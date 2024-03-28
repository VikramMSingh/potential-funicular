people_list=["Vik", "Shal", "Sid", "Mo", "Gha", "Lul"]

language_poll = {"Vik":"Python", "Shal":"C++", "Sid":"R","Gha":"Tableau"}


for ppl in people_list:
   # print(f"{ppl}")
    
    if ppl in language_poll:
        print(f"{ppl}'s favorite language is {language_poll[ppl]}")
    else:
        print(f"{ppl} please take the poll and decide your favorite programming language")
    


#for name in people_list:
#    if name,value in language_poll:
#        print(f"{name}'s favorite language is {value}")
#    else:
#        print(f"{name}, please take the poll")
