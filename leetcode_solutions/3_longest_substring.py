# ...existing code...
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Summary:
        # Return the length of the longest substring without repeating characters.
        # Uses a sliding-window approach with a set to track characters in the window.
        
        # 'exists' holds the characters currently inside the sliding window (no duplicates).
        exists = set()
        # 'left' is the start index of the window; 'max_length' stores the best window size seen.
        left, max_length = 0, 0

        # Use 'i' as the end index of the window and expand one character at a time.
        for i in range(len(s)):
            # If s[i] is already in the window, shrink the window from the left
            # until the duplicate character is removed.
            while s[i] in exists:
                exists.remove(s[left])  # remove the leftmost char from the window
                left += 1               # move window start rightwards

            # Add the current character to the window (now guaranteed unique inside window).
            exists.add(s[i])

            # Update maximum length: current window size is (i - left + 1).
            # Window runs from index `left` to `i` inclusive, so size is (i - left + 1)
            # because indices are zero-based and both ends count.
            max_length = max(max_length, i - left + 1)

        # Return the length of the longest substring found without repeating chars.
        return max_length
