def binary_search(arr, min, max, num):
    if max >= min:
        mid = (max+min)//2
     
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            return binary_search(arr, mid+1, max, num)
        elif num < arr[mid]:
            return binary_search(arr, min, mid-1, num)
        else:
            return "Number not found"
    print(f"{num} is at index {mid}") 
a = int(input("Enter a number: "))
aray = [1,3,4,5,6,7,9,11,23,122,342,398,402]

r=binary_search(aray, 0, len(aray) - 1, a)
print(f"Found {a} at index {r}") 
