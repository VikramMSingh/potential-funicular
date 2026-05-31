from collections import defaultdict  # defaultdict creates lists for missing keys automatically

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
        # Sort words inside each group and sort groups so comparisons are order-insensitive
        return sorted([sorted(g) for g in groups])

    for inp, expected in test_cases:
        out = sol.groupAnagrams(inp)
        if normalize(out) == normalize(expected):
            print(f"PASS: {inp} -> {out}")
        else:
            print(f"FAIL: {inp} -> {out}, expected {expected}")
            raise SystemExit(1)

    print("All tests passed")

