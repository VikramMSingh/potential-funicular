class Solution:
    def longestValidParentheses(self, s: str) -> int:
    # Variable to store the longest valid parentheses
        count = 0
    # Left counter will count the number of '('
        left = 0
    # Right counter will count the number of ')'
        right = 0
    # Loop through the string from left to right.
    # This will take care of extra right parentheses
        for i in range(len(s)):
            # Current character
            c = s[i]
            if c == '(':
                left += 1
            if c == ')':
                right += 1
        # If both left and right are equal,
        # it means we have a valid substring
            if left == right:
                count = max(count, left + right)
        # If right is greater than left,
        # it means we need to set both
        # counters to zero
            if right > left:
                left = right = 0
    # Reset left and right
        left = right = 0
    # Follow the same approach but now loop the string
    # from right to left. This will take care of extra
    # left parentheses
        for i in range(len(s) - 1, -1, -1):
        # Current character
            c = s[i]
            if c == '(':
                left += 1
            if c == ')':
                right += 1
        # If both left and right are equal,
        # it means we have a valid substring
            if left == right:
                count = max(count, left + right)
        # If right is greater than left,
        # it means we need to set both
        # counters to zero
            if left > right:
                left = right = 0
        return count
