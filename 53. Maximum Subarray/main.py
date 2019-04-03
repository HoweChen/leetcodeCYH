class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # method 1
        # 当前一个数是正数的时候才相加，保证 和 一直在往上走
        # 也是dp的思想，把现在的index所遇到的数，和之前遇到的数们组成的子列表的最大值进行比较
        # 这个时候才修改当前值
        # 最后取最大
        # O(n)
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
