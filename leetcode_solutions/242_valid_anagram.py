# ...existing code...
class Solution:  # LeetCode expects a Solution class with method isAnagram
    def isAnagram(self, s: str, t: str) -> bool:  # method signature: two strings in, boolean out
        if len(s) != len(t):  # if lengths differ they cannot be anagrams
            return False  # early exit for unequal lengths
        count = {}  # dictionary to store character frequencies from s
        for char in s:  # iterate each character in s
            count[char] = count.get(char,0)+1  # increment count for this character (init to 0 if missing)
        for char in t:  # iterate each character in t to "cancel out" counts
            if char not in count or count[char] == 0:  # if char absent or already used up, t has extra/mismatched char
                return False  # not an anagram
            count[char] -= 1   # decrement the count for this character
        return True  # all characters matched; strings are anagrams