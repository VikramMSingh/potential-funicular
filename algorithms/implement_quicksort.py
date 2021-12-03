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
    temp = arr[0]
    arr[0] = arr[p]
    arr[p] = temp
    left = quick_sort(arr[0:p])
    right = quick_sort(arr[p+1:l])
    arr = left + [arr[p]] + right
    return arr
ar = [7,1,4,8,6,8,9]
r = quick_sort(ar)
print(f"Sorted array is : {r}")
    
