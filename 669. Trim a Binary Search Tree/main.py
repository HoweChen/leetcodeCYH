# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
        # 调用顺序：
        # 1.left = trim(1.left = 0)
        # return trim(0.right = None)
        # return None
        # 返回结果即为 1.left = None
