# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def traverse(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = ListNode(nums[mid])
            node.left = traverse(nums[:mid])
            node.right = traverse(nums[mid+1:])
            return node

        return traverse(nums)
