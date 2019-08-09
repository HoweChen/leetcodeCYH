# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node,lvs):
            if node:
                if not node.left and not node.right:
                    # print(lvs)
                    lvs.append(node.val)
                    # print(lvs)
                else:
                    lvs = bfs(node.left,lvs)
                    lvs = bfs(node.right,lvs)
            return lvs
                
        if not root1 or not root2:
            return False
        elif not root1 and not root2:
            return True
        else:
            # lvs stores value instead of node
            lvs_1 = []
            lvs_2 = []
            lvs_1 = dfs(root1,lvs_1)
            lvs_2 = dfs(root2,lvs_2)
            return lvs_1 == lvs_2
    
        