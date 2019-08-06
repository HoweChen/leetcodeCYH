# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # method 1:
        if not root:
            return 0
        if (root.val < L):
            return self.rangeSumBST(root.right,L,R)
        if (root.val > R):
            return self.rangeSumBST(root.left,L,R)
        return root.val+self.rangeSumBST(root.left,L,R)+self.rangeSumBST(root.right,L,R)
        
        # method 2:
        # if not root:
        #     return 0
        # else:
        #     value = 0
        #     if L<=root.val<=R:
        #         value = root.val
        #     else:
        #         pass
        #     return value +self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)