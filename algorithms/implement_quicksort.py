def quick_sort(arr):
    l = len(arr)
    if l < 2: 
        return arr
    p = 0 #Partition at the beginning 
    
    for i in range(1, l):
        if arr[i] <= arr[0]:
            p += 1 
            temp = arr[i]
            arr[i] = arr[p]
            arr[p] = temp
            print(f"p:{p}, {arr[i]}, {arr[p]}, {temp}")
    temp = arr[0]
    arr[0] = arr[p]
    arr[p] = temp
    print(f"p is {p}")
    left = quick_sort(arr[0:p])
    right = quick_sort(arr[p+1:l])
    arr = left + [arr[p]] + right
    return arr
ar = [5,2,4,7,6,9]
r = quick_sort(ar)
print(f"Sorted array is : {r}")
    
