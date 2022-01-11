def mergeSortedLL(list1, list2):
    last = 0
    third = last
    while list1 != None and list2 != None:
        if list1.data < list2.data:
            last.next = list1
            list1 = list1.next            
        else:
            last.next = list2
            list2 = list2.next
        last = last.next
    last.next = list1 or list2
    return third.next

