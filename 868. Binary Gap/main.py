class Solution:
    def binaryGap(self, N: int) -> int:
        n_bin_list = list(bin(N))[2::]
        # remove useless prefix 0s
        n_bin_list = n_bin_list[n_bin_list.index("1")::]

        # method 1: 用stack，碰到第二个1就获取stack长度跟已知最大进行比较
        # stack = []
        # result = 0
        # for i in range(len(n_bin_list)):
        #     if n_bin_list[i] == '0':
        #         if stack:
        #             stack.append("0")
        #         else:
        #             continue
        #     if n_bin_list[i] == "1":
        #         if stack:
        #             result = max(len(stack),result)
        #             stack.clear()
        #         stack.append("1")
        # return result

        # method 2: 找出所有1出现的位置，然后计算彼此之间最大的距离
        index_list = [index for index, value in enumerate(
            n_bin_list) if value == "1"]
        return max([(b-a) for a, b in zip(index_list, index_list[1:])] or [0])

        # method 3:
        # A = [i for i in range(32) if (N >> i) & 1]
        # if len(A) < 2: return 0
        # return max(A[i+1] - A[i] for i in range(len(A) - 1))
