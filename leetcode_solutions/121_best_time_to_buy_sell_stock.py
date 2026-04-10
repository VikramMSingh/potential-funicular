class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = float(inf)
        m = 0 
        for i in prices:
            p = min(p,i)
            m = max(m,i-p)
        return m