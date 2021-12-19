def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        a = list(s.rstrip())
        l = len(a)
        count = 0
        for i in range(l-1, -1, -1):
            if a[i].isalpha():
                count += 1
            else:
                break 
                
        return count

word = input("Enter any word or sentence - ")
solution = lengthOfLastWord(word)

print(solution)
