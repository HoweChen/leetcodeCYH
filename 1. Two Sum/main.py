class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            another_num = target-num
            index = nums.index(num)
            if another_num in nums[index+1:]:
                result = [nums.index(num), nums[index+1:].index(another_num)+index+1]
                break
        return result
