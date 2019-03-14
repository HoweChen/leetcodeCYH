class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:

        # method 1: 正像比较
        #         flags = []
        #         for index, value in enumerate(S):
        #             if value == C:
        #                 flags.append(index)

        #         result = []

        #         # 先比从S开头到第一个index
        #         for index in range(flags[0]):
        #             result.append(flags[0]-index)
        #         #print(flags)
        #         #print(result)

        #         # 比第一个index到最后一个index
        #         for j in range(1,len(flags)):
        #             for i in range(flags[j-1],flags[j]):
        #                 # 3,4
        #                 result.append(min(abs(flags[j-1]-i),abs(flags[j]-i)))
        #         #print(result)

        #         # 比最后一个index到S尾
        #         for index in range(flags[-1],len(S)):
        #             result.append(index-flags[-1])
        #         #print(result)
        #         return result

        # method 2: 双向比较 跟 method 1 速度一样，但是在现实中可拓展成多进程
        from itertools import chain  # 这里要用itertool里的chain
        # 因为在python2里 range() 返回list
        # python3 里range 返回iterator，不能直接相加，要用chain方法
        n = len(S)
        res = [n] * n
        pos = -n
        for i in chain(range(n), range(n)[::-1]):  # 这个写法可以实现一个for里双向遍历
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res
