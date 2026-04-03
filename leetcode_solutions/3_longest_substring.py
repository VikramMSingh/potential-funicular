class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exists = set()
        left,max_length = 0,0
        for i in range(len(s)):
            while s[i] in exists:
                exists.remove(s[left])
                left += 1
            exists.add(s[i])
            max_length = max(max_length, i - left + 1)
        return max_length
       

        