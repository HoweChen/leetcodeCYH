class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        original = set(range(len(nums)+1))
        nums = set(nums)
        return original.difference(nums).pop()


test_list = [9, 6, 4, 2, 3, 5, 7, 0, 1]
a = Solution().missingNumber([0])
print(a)
