 class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1 #define int min and max
        i, n = 0, len(s) #initialize pointers

    # 1. skip leading whitespace
        while i < n and s[i] == ' ': #ignore leading whitespace
            i += 1

    # 2. optional sign
        sign = 1
        if i < n and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1 #assign value
            i += 1 #skip past the sign

    # 3. read digits
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

    # 4. apply sign and clamp
        result *= sign
        return max(INT_MIN, min(INT_MAX, result))