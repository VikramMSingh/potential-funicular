def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        max_profit = 0
        max_curr = 0 
        min_price = prices[0]
        for i in range(l):
            min_price = min(min_price, prices[i])
            max_curr = max(0, prices[i] - min_price)
            max_profit = max(max_profit, max_curr)
        return max_profit


p = [3,1,2,5,6,7,4]
solution = maxProfit(p)

print(solution)
