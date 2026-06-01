from collections import Counter
from typing import List

class Solution:
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        """
        Return the k most frequent elements in nums.

        Approach:
        - Count frequencies using Counter.
        # - Use a bucket-sort style list "freq" where index represents frequency'////// ..//./././/;/.l>
          (freq[i] is a list of numbers that appear i times).
        - Iterate buckets from highest frequency to lowest and collect numbers
          until we have k results.

        Time complexity: O(n) on average (counting + bucket construction + scanning)
        Space complexity: O(n) for the counter and buckets.
        """
        count = Counter(nums)
        # Create buckets where index represents the frequency
        freq = [[] for i in range(len(nums)+1)]
        #print(freq)
        for n,c in count.items():
            # place number n in the bucket corresponding to its count c
            freq[c].append(n)
        print(freq)
        
        res=[]
        # iterate from highest possible frequency down to 1
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                # add numbers with current frequency
                res.append(n)
                # stop early once we've collected k elements
                if len(res)==k:
                    return res
        
    if __name__ == "__main__":
        assert sorted(topKFrequent([1,1,1,2,2,3], 2)) == [1,2]
        assert topKFrequent([1], 1) == [1]
        print("Heap solution passed")