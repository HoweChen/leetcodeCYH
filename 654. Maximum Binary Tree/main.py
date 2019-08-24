# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 传统解法，利用递归，通过了
        # if not nums:
        #     return None
        # max_num = max(nums)
        # index = nums.index(max_num)
        # root = TreeNode(max_num)
        # root.left = self.constructMaximumBinaryTree(nums[0:index:])
        # root.right = self.constructMaximumBinaryTree(nums[index+1::])
        # return root

        # 这个方法的思想是利用堆栈，保证堆栈从顶到底部是增大的，在python的list里看来就是从左到右是递减的
        stack = []
        last = None

        for num in nums:

            while stack and stack[-1].val < num:
                last = stack.pop()  # 找出堆栈当中已经存储的小于这个新的值的最大节点

            node = TreeNode(num)

            if stack:
                # 如果这时候堆栈里头还有节点，说明堆栈里的这个节点比新的值大，只要是大的都把新的值放在node的右边
                stack[-1].right = node

            if last:
                node.left = last  # 那么剩下的这个比新的值小的，就放在左边

            stack.append(node)  # 把新的值压入堆栈，这样子没个堆栈里的成员，都存储着连着别的节点的信息
            last = None

        return stack[0]
