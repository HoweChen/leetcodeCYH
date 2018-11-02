class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(sorted(A), key=lambda x: x % 2 == 0, reverse=True)


sol = Solution()
A = [3, 1, 2, 4]
output = [2, 4, 1, 3]
output2 = [2, 4, 1, 3]
assert sol.sortArrayByParity(A) == output2
print(sol.sortArrayByParity(A))
