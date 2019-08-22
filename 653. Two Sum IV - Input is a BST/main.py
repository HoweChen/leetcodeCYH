# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        # dfs recursive
#         def dfs(node):
#             if node:
#                 table.add(node.val)
#                 dfs(node.left)
#                 dfs(node.right)
#             else:
#                 return
            
 
#         if not root:
#             return False
        
#         table = set()
#         dfs(root)
#         for num in table:
#             target = k-num
#             if target in table and target != num:
#                 return True
#         return False

        # bfs iterative
        def bfs(node):
            stack = [node]
            for node in stack:
                if (k-node.val) in table:
                    return True
                else:
                    table.add(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            return False
        
        if not root:
            return False
        table = set()
        return bfs(root)