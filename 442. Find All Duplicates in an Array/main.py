class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # method 1: set
        # pool = set()
        # pool_len = len(pool)
        # result = []
        # for num in nums:
        #     pool.add(num)
        #     if len(pool) == pool_len:
        #         result.append(num)
        #     else:
        #         pool_len = len(pool)
        # return result

        # method 2: sort then check, a little bit slower then method 1
        # nums = sorted(nums)
        # result = []
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         result.append(nums[i])
        # return result

        # method 3: counter, use collections. Better then method 1 and 2
        # import collections
        # return [item for item, count in collections.Counter(nums).items() if count >1]

        # method 4: use True or False list to determine if the number has been seen
        # Best answer so far
        seen = [False] * (len(nums) + 1)
        result = []
        for num in nums:
            if seen[num] is True:
                result.append(num)
            else:
                seen[num] = True

        return result
