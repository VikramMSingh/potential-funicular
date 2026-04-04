# ...existing code...
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine whether the input string of brackets is valid.

        A string is valid if:
        - Every opening bracket has a corresponding closing bracket of the same type.
        - Brackets are closed in the correct order (LIFO).

        Time complexity: O(n) where n = len(s). Each character is processed once.
        Space complexity: O(n) in the worst case for the stack (e.g., all opening brackets).
        """
        stack = []  # stack to hold opening brackets as we encounter them
        matches = {')': '(', '}': '{', ']': '['}  # map each closing bracket to its opening

        for ch in s:
            # If ch is an opening bracket, push it onto the stack
            if ch in '({[':
                stack.append(ch)
            else:
                # ch is a closing bracket:
                # - if stack is empty there is no matching opening bracket -> invalid
                # - if top of stack is not the corresponding opening bracket -> invalid
                if not stack or stack[-1] != matches[ch]:
                    return False
                # Found a matching opening bracket, pop it
                stack.pop()

        # If stack is empty, all opening brackets were matched; otherwise invalid
        return len(stack) == 0