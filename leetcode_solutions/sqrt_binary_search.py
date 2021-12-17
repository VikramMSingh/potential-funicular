class Solution:
    def mySqrt(x):
        l = 0
        r = x 
        mid = 0 
        while l <= r:
            mid = (l + r)//2
            if mid*mid > x:
                r = mid - 1 
            elif mid*mid < x:
                l = mid + 1
            else:
                return mid 
        return r

a = Solution.mySqrt(6)
print(a)
