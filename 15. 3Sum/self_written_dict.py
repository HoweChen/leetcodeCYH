class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


test_cases = [[-1, 0, 1, 2, -1, -4], [0, 0, 0],
              [0, 0, 0, 0], [1, -1, 2, -2], [], [0], [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0], [4, 4, 3, -5, 0, 0, 0, -2, 3, -5, -5, 0]]
sol = Solution()
for case in test_cases:
    print(sol.threeSum(case))
