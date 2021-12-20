def minOperations(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = prev = 0
        for cur in nums:
            if cur <= prev:
                prev += 1
                count += prev - cur
            else:
                prev = cur
        return count
    
sample_array = [1,7,2,4,4]
solution = minOperations(sample_array)
print(solution)
