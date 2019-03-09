class Solution:
    @staticmethod
    def is_odd(num):
        if (num & 1) == 1:
            return True
        else:
            return False

    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:

        # method 1: 超时
        # result = []
        # for num, index in queries:
        #     A[index] = A[index]+num
        #     result.append(sum([x for x in A if x%2==0]))
        # return result

        # method 2:
        # 想法是用一张表记录所有的偶数位的情况
        # 通过但是速度很慢

        #         result = []
        #         odd = {}
        #         even = {}
        #         A_len = len(A)

        #         for index in range(A_len):
        #             if self.is_odd(A[index]) is True:
        #                 odd[index]=A[index]
        #             else:
        #                 even[index] = A[index]
        #         for num, index in queries:
        #             if index in odd.keys():
        #                 if self.is_odd(num) is True:
        #                     # odd + odd = even
        #                     even[index]=odd[index]+num
        #                     del(odd[index])

        #                 else:
        #                     # odd + even = odd
        #                     odd[index]+=num

        #             else:
        #                 # index in even.keys()
        #                 if self.is_odd(num) is True:
        #                     # even + odd = odd
        #                     odd[index]=even[index]+num
        #                     del(even[index])
        #                 else:
        #                     # even + even = even
        #                     even[index]+=num

        #             result.append(sum(even.values()))
        #         return result
        # method 3:
        S = sum(x for x in A if x % 2 == 0)

        for counter, elem in enumerate(queries):

            val, index = elem

            if self.is_odd(A[index]) is False:
                S -= A[index]

            A[index] += val

            if self.is_odd(A[index]) is False:
                S += A[index]

            queries[counter] = S

        return queries
