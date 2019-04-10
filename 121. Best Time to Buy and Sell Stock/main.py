class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # method 1
        # 因为是股票交易，有时间的因素，所以我们要保证在当前最小的波谷买入，然后在后续的波峰卖出
        # 不能用min，是因为有可能整个数组的最小值之后的序列收益很小，所以应该记录当前已遍历的数组的最小值
        if not prices:
            return 0
        else:
            min_now = prices[0]
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] < min_now:
                    min_now = prices[i]
                else:
                    profit = max(profit, prices[i]-min_now)
            return profit
