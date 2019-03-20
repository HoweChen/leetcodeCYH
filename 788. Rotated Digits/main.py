class Solution:
    # for method 1 only
    # def __init__(self):
    #     # look up table
    #     self.true_LUT ={
    #         "2":"5",
    #         "5":"2",
    #         "6":"9",
    #         "9":"6"
    #     }
    #     self.false_LUT = {
    #         "0":"0",
    #         "1":"1",
    #         "8":"8"
    #     }
    #     self.invalid_LUT = ["3","4","7"]

    def rotatedDigits(self, N: int) -> int:
        # method: compare bit by bit, brute force
        #         digits = list(map(str,(range(1,N+1))))
        #         count = 0
        #         for num_str in digits:
        #             if is_good_number(num_str) is True:
        #                 count+=1
        #         return count

        #         def is_good_number(self,num_str):
        #             tmp = list(num_str)
        #             tmp_len = len(tmp)
        #             if len(tmp)>1:
        #                 for i in range(tmp_len):
        #                     if tmp[i] in self.invalid_LUT:
        #                         return False
        #                     if tmp[i] in self.true_LUT.keys():
        #                         tmp[i] = self.true_LUT[tmp[i]]
        #                 if "".join(tmp) == num_str:
        #                     print(tmp,num_str)
        #                     return False
        #                 else:
        #                     return True
        #             else:
        #                 if num_str in self.invalid_LUT or num_str in self.false_LUT.keys():
        #                     return False
        #                 else:
        #                     return True
        # method 2
        # s1 = set([1, 8, 0])
        # s2 = set([1, 8, 0, 6, 9, 2, 5])
        # def isGood(x):
        #     s = set([int(i) for i in str(x)])  # 把所有的数字set化成 0-9
        #     return s.issubset(s2) and not s.issubset(s1)
        # return sum(isGood(i) for i in range(N + 1))  # use sum to sum up the true answer

        # method 3
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        res = 0
        N = list(map(int, str(N)))
        for i, v in enumerate(N):
            print(i, v)
            for j in range(v):
                print(j)
                if s.issubset(s2) and j in s2:
                    res += 7**(len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3**(len(N) - i - 1)
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))
