def partition(arr):
    l = 0
    h = len(arr) - 1
    p = arr[l]
    i = l
    j = h
    while i < j:
        if arr[i] <= p:
            i = i+1
        if arr[j] > p:
            j = j - 1
        if i > j:
            arr[i], arr[j] = arr[j],arr[i]
    arr[l], arr[j] == arr[j], arr[l]
    return j

def quickSort(arr):
    l = 0 
    h = len(arr) - 1
    if l < h:
        x = partition(arr)
        quickSort(arr[l:x+1])
        quickSort(arr[x+1:h])
    
a = [2,5,4,7,6,9]

print(quickSort(a))

