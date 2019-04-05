class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # method 1:
        # two ptr
        start_point = None
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                if start_point is None:
                    start_point = prices[i-1]
            else:
                # list decrease
                if start_point is not None:
                    profit += prices[i-1] - start_point
                    start_point = None
        if start_point is not None:
            profit += prices[-1] - start_point
        return profit
