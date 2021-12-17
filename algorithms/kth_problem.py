def findKthPositive(arr, k):
    low = 0
    high = len(arr) 
    mid = (low + high)//2
    while high > low:
        if arr[mid] - (mid + 1) >= k:
            high = mid
        else:
            low = mid + 1
            
    return low + k

ls = [2,3,4,7,11]
r = 5
ans = findKthPositive(ls,r)
print(ans)
