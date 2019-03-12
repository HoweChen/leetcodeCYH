class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # method 1: 重新复线游戏的规则
        # 这里运用到了 python deque 的rotate 功能，把这个index从后面rotate到第一位
        # 这里相当于把游戏规则给反过来，所以我们要用reverse来把排序好的数组给反过来
        d = collections.deque()
        for x in reversed(sorted(deck)):
            d.rotate()
            d.appendleft(x)
        return list(d)
