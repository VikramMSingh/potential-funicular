class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum = sum(nums[:k])
        m_sum = k_sum
        for i in range(k, len(nums)):
            k_sum += nums[i]
            k_sum -= nums[i-k]
            m_sum = max(m_sum,k_sum)
        return m_sum/k