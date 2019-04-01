class Solution:

    def bs(self, nums: List[int], target: int)->int:
        if len(nums) == 1:
            return nums[0]
        else:
            pivot = len(nums) // 2

            if target >= nums[pivot]:
                return self.bs(nums[pivot:], target)
            else:
                return self.bs(nums[0:pivot], target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        # method 1
        # using binary search
        bs_result = self.bs(nums, target)
        index = nums.index(bs_result)
        if target > bs_result:
            return index+1
        else:
            return index

        # method 2:
        # bi-directional pointer
#         if nums is None or len(nums) == 0:
#             return 0
#         if target is None:
#             return None
#         left, right = 0, len(nums) - 1
#         while left + 1 < right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid
#             else:
#                 right = mid

#         if nums[left] >= target:
#             return left
#         elif nums[right] >= target:
#             return right
#         else:
#             return right + 1

        # method 3: intuition method, tranverse the list
        # for i in range(len(nums)):
        #     if target <= nums[i]:
        #         return i
        # return len(nums)
