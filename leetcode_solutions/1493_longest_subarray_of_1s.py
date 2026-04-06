# ...existing code...
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix string amongst an array of strings.

        (Docstring retained for API/help; see inline comments below for a
        student-friendly step-by-step explanation.)
        """
        # Explanation for a student (step-by-step) as inline comments:
        # 1) If the input list is empty, there is no common prefix -> return "".
        # 2) Use the first string as a reference. Any common prefix cannot be
        #    longer than this reference string.
        # 3) Iterate over each index i in the reference string:
        #      - Let c = first[i].
        #      - For every other string in the list:
        #          a) If i is out of range for that string (i >= len(other)),
        #             that string is shorter than the current prefix candidate,
        #             so return first[:i] — the longest common prefix found so far.
        #          b) If other[i] != c, characters differ at position i, so return
        #             first[:i] as the longest common prefix.
        # 4) If we finish the loop without finding any mismatch, the entire first
        #    string is the common prefix -> return it.
        #
        # Complexity:
        # - Time: O(S) where S is the sum of lengths of all strings. We compare
        #   characters position-by-position and each character is compared at most once.
        # - Space: O(1) extra space (excluding the space for the returned prefix).
        #   The returned slice first[:k] creates a new string of length k (output size).

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
#