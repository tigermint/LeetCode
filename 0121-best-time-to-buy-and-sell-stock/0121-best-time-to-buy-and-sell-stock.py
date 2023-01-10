class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s, profit = prices[0], 0, 0
        for s in range(0, len(prices)):
            # b 검사
            if prices[s] < b:
                b = prices[s]
            # profit 검사
            if prices[s] - b > profit:
                profit = prices[s] - b
        return profit
        
        