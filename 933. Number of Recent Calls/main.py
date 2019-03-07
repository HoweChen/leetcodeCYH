class RecentCounter:
    # 这题的关键在于是一个滑动的窗口，这个窗口大小是t-3000,t，在dq里的数字只要超出这个就要被剔除
    # 每一次调用就要返回这个dq的长度

    def __init__(self):
        from collections import deque
        self.dq = deque()

    def ping(self, t: int) -> int:
        self.dq.append(t)
        while self.dq[0] < t-3000:
            self.dq.popleft()
        return len(self.dq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
