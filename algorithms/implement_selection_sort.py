def selection_sort(arr):
    l = len(arr)
    n = 0
    for i in range(n,l):
        for j in range(n+1, l):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                n += 1
    return arr

ls = [2,3,4,1,8,7,5]
r = selection_sort(ls)

print(f"Sorted list - {r}")
