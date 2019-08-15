# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode,val=0) -> int:
        def dfs(node, prefix):
            if node:
                new_prefix = node.val + (prefix << 1)

                if node.left or node.right:
                    return dfs(node.left, new_prefix) + dfs(node.right, new_prefix)
                else:
                    return new_prefix
            else:
                return 0

        return dfs(root, 0)
                
        