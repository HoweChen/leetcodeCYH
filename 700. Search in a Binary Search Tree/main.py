# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            depth = 1
            depth = self.getDepth(root, depth)
            return depth+1

    def getDepth(self, root, depth):
        if root.left is None and root.right is None or not root:
            depth -= 1
        elif root.left is None:
            # goto the right subtree
            depth += self.getDepth(root.right, depth + 1)
        elif root.right is None:
            depth += self.getDepth(root.left, depth + 1)
        else:
            depth = self.getDepth(root.left, depth + 1)
            depth = self.getDepth(root.right, depth + 1)
        return depth
