class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = {}
        nums = sorted(nums)
        result_num = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                target_num = -(i+j)
                target_list = sorted([nums[i], nums[j], target_num])
                if target_num in nums[j::] and target_list not in result.values():
                    result[result_num] = target_list
                    result_num += 1

        print(result)
        return sorted(list(result.values()))


test_cases = [[-1, 0, 1, 2, -1, -4], [0, 0, 0],
              [0, 0, 0, 0], [1, -1, 2, -2], [], [0]]
sol = Solution()
for case in test_cases:
    print(sol.threeSum(case))
