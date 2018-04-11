class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            index=0
            flag = None
            while(index!=len(nums)):
                if nums[index]!=flag:
                    flag = nums[index]
                    index+=1
                else:
                    nums.remove(nums[index])
            return len(nums)
