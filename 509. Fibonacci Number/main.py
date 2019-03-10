class Solution:

    def __init__(self):
        self.fib_cache = dict()

    def fib(self, N: int) -> int:
        # method 1: recursive
        # if N<=1:
        #     return N
        # else:
        #     result = self.fib(N-1)+self.fib(N-2)
        #     return result

        # method 2: using dict cache
        # if N<=1:
        #     return N
        # else:
        #     if N in self.fib_cache.keys() is True:
        #         return self.fib_cache[N]
        #     else:
        #         result = self.fib(N-1)+self.fib(N-2)
        #         self.fib_cache[N] = result
        #         return self.fib_cache[N]

        # method 3: iterative
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a+b
        return a
