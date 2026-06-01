"""
Group Anagrams

This module implements Solution.groupAnagrams, which groups a list of strings into
lists of anagrams. The core idea is to use a canonical key for each word: the
sorted sequence of its characters. All words with the same sorted key are
anagrams and are collected into the same bucket.

Algorithm complexity:
- Time: O(N * K log K) where N is number of strings and K is average word length
  (sorting each word costs O(K log K)).
- Space: O(N * K) to store the grouped words and keys.

A small test harness is included under the usual "if __name__ == '__main__'"
guard. Tests normalize groups and contents before comparing, so ordering of
groups and words inside groups does not affect equality checks.
"""

from collections import defaultdict  # defaultdict creates lists for missing keys automatically

# High-level overview:
# The algorithm groups words that are anagrams by computing a canonical key
# for each word: the characters sorted into a string. All words sharing the
# same sorted key are collected into the same bucket (list). The result is
# a list of those buckets. Note: ordering of groups and items within groups
# is not guaranteed by this implementation.

class Solution:
    def groupAnagrams(self, strs):
        # strs: list of input strings to group into anagram buckets

        # Create a map where each key is the canonical sorted form of a word
        # and the value is a list of original words that match that key.
        anagram_map = defaultdict(list)

        # Iterate over each word in the input list
        for word in strs:
            # Sort the characters of the word to create a canonical key.
            # Example: "eat" -> ['a','e','t'] -> "aet"; all anagrams share this key.
            sorted_key = "".join(sorted(word))

            # Append the original word to the list corresponding to the sorted key.
            # defaultdict ensures an empty list is created for a new key automatically.
            anagram_map[sorted_key].append(word)

        # Convert the dict values (lists of anagrams) to a list and return.
        # The order of groups and words within groups is not guaranteed.
        return list(anagram_map.values())

if __name__ == "__main__":
    # Basic test cases to verify groupAnagrams behavior
    test_cases = [
        (['eat', 'tea', 'tan', 'ate', 'nat', 'bat'], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
        ([''], [['']]),
        (['a'], [['a']]),
    ]

    sol = Solution()

    def normalize(groups):
        # Normalize helper: sort words inside each group and then sort groups so
        # comparisons in tests do not depend on ordering. This allows tests to
        # verify grouping correctness without requiring deterministic ordering.
        return sorted([sorted(g) for g in groups])

    for inp, expected in test_cases:
        out = sol.groupAnagrams(inp)
        if normalize(out) == normalize(expected):
            # Print a concise success line for the given input case
            print(f"PASS: {inp} -> {out}")
        else:
            # On failure, show expected vs actual to aid debugging and exit
            print(f"FAIL: {inp} -> {out}, expected {expected}")
            raise SystemExit(1)

    # If all cases succeed, emit a final confirmation message
    print("All tests passed")

