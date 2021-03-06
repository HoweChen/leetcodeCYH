# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1::]:
            node = TreeNode(value)
            if value < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()  # 这里需要一直pop是要找到比要插入的值小的最适合的点
                last.right = node
                stack.append(node)
        return root
