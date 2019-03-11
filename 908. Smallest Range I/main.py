class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        # method 1:

        #         if len(A) <=1:
        #             return 0
        #         else:
        #             length = len(A)
        #             avg = min(A)+K
        #             for index in range(length):
        #                 diff = abs(avg-A[index])
        #                 if diff == 0:
        #                     continue
        #                 else:
        #                     if diff <=K:
        #                         A[index] = avg
        #                     else:
        #                         if A[index]<avg:
        #                             A[index] += K
        #                         else:
        #                             A[index] -= K

        #             print(A)
        #             return max(A)-min(A)

        # method 2: solution
        return max(0, max(A) - min(A) - 2*K)
