class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(i) for i in zip(*A)]


sol = Solution()

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A_Sol = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

B = [[1, 2, 3], [4, 5, 6]]
B_Sol = [[1, 4], [2, 5], [3, 6]]

assert sol.transpose(A) == A_Sol
assert sol.transpose(B) == B_Sol
