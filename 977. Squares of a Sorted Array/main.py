class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # method 1
        # return sorted(map(lambda x: x**2, A))
        return sorted(x*x for x in A)

        # method 2
        # 第二个方法利用了两个指针从最接近于0的数字开始向两边扩散
#         N = len(A)
#         # i, j: negative, positive parts
#         j = 0
#         while j < N and A[j] < 0:
#             j += 1
#         i = j - 1

#         ans = []
#         while 0 <= i and j < N:
#             if A[i]**2 < A[j]**2:
#                 ans.append(A[i]**2)
#                 i -= 1
#             else:
#                 ans.append(A[j]**2)
#                 j += 1

#         while i >= 0:
#             ans.append(A[i]**2)
#             i -= 1
#         while j < N:
#             ans.append(A[j]**2)
#             j += 1

#         return ans
