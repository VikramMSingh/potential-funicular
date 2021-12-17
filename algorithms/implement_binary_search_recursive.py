def BSR(arr,l,h,key):
    if l == h:
        if arr[l] == key:
            return l 
        else: 
            return "Not found"
    else:
        mid = (l+h)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return BSR(arr, l, mid-1, key)
        elif key > arr[mid]:
            return BSR(arr, mid+1, h, key)
        else:
            return "Not Found"

ar = [1,2,3,4,6,7,9,11,24,25,26,27,110,223,1230]
l = 0 
h = len(ar) - 1

key = int(input("Enter a random number: "))

ans = BSR(ar, l, h, key)

print(f"Number is at {ans}") 
