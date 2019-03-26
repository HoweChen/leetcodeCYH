class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # method 1: use Counter
        # time = len(nums)//2
        # from collections import Counter
        # nums = Counter(nums)
        # for value, count in nums.items():
        #     if count> time:
        #         return value

        # method 2: tranverse the list and record the count of each num
        seen = []
        maximum = len(nums)//2
        for num in nums:
            if num not in seen:
                count = nums.count(num)
                if count > maximum:
                    return num
                else:
                    seen.append(num)
        return maximum
