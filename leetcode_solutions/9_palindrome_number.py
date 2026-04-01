class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        n = x
        while n > 0:
            digit = n%10
            y = (y*10)+digit
            n //= 10
        if x < 0: 
            return False
        elif x == y:
            return True
        else:
            return False
        
