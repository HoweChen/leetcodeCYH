class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # method 1:
        min_cost0, min_cost1 = cost[0], cost[1]
        for c in cost[2:]:
            # 思路是把下一个cost加上上两步当中消耗最小的那一个
            min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + c
        return min(min_cost0, min_cost1)

        # method 2:
        # method 1 的不同的写法，但是思路是一样的，
        # for i in range(2,len(cost)):
        #     cost[i] += min(cost[i-1],cost[i-2])
        # return min(cost[-1],cost[-2])
