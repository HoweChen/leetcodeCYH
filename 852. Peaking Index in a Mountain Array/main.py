class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # my solution
        return A.index(max(A))

        # 二分法的解法
        # if len(A) == 1:
        #     return 0
        # if len(A) == 2:
        #     if A[0] > A[1]:
        #         return 0
        #     return 1
        # mid  = len(A)//2
        # print(mid)
        # if A[mid-1] > A[mid]:
        #     num = self.peakIndexInMountainArray(A[0:mid])
        #     return num
        # elif A[mid+1] > A[mid]:
        #     num = self.peakIndexInMountainArray(A[mid+1:])
        #     return num + 1 + mid
        # else:
        #     return mid


sol = Solution()
A = [0, 1, 0]
B = [0, 2, 1, 0]
print(sol.peakIndexInMountainArray(A))
print(sol.peakIndexInMountainArray(B))
