class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # method 1:
        # sort the array, then eigher the leftmost number(when negative occurs) multiply rightmost or rightmost three numbers
        # nums = sorted(nums)
        # return max(nums[0]*nums[1]*nums[-1],nums[-3]*nums[-2]*nums[-1])

        # method 2:
        max1, max2, max3, min1, min2 = float(
            '-Inf'), float('-Inf'), float('-Inf'), float('Inf'), float('Inf')
        for num in nums:
            if num >= max1:
                max3, max2, max1 = max2, max1, num
            elif num >= max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num
            if num <= min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num
        return max(max1*max2*max3, min1*min2*max1)

        # method 3: best but use python's library
        # same idea as method 2 but use python's heapq
        # import heapq
        # return max(nums) * max(a * b for a, b in [heapq.nsmallest(2, nums), heapq.nlargest(3, nums)[1:]])
