from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix string amongst an array of strings.

        Explanation for a student (step-by-step):
        1. If the input list is empty, there is no common prefix -> return "".
        2. Use the first string as a reference. We'll check each character position i
           across all other strings.
        3. For each index i in the first string:
           - For each other string, check two things:
             a) Is i already past the end of that string? If yes, that string is shorter
                than the prefix considered so far, so stop and return the prefix up to i.
             b) Does the character at position i differ from the first string's char?
                If yes, stop and return the prefix up to i.
        4. If we finish checking all characters of the first string without a mismatch,
           then the whole first string is the common prefix -> return it.

        Complexity:
        - Time: O(S) where S is the sum of all characters in all strings.
          We potentially examine each character of each string at most once.
        - Space: O(1) extra space (not counting input/output). We only use indices and
          return a slice of an existing string.
        """
        # Handle empty input
        if not strs:
            return ""

        # Use first string as reference
        first = strs[0]

        # Iterate over each index in the reference string
        for i in range(len(first)):
            c = first[i]
            # Compare character at i with the i-th character of all other strings
            for other in strs[1:]:
                # If i is out of range for other, or characters differ -> stop
                if i >= len(other) or other[i] != c:
                    return first[:i]
        # If no mismatch found, entire first string is common prefix
        return first