def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        left = 0 
        right = l - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s 

### Example execution
string = ['H','e','y','f','r','i','e','n','d']
solution = reverseString(string)
print(f"Reverse string : {solution}")
