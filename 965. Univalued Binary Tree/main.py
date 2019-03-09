# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # method 1: deep first search
        # def dfs(node,target):
        #     if node:
        #         #print(node.val,target)
        #         if node.val !=target:
        #             return False
        #         else:
        #             l_result = dfs(node.left,target)
        #             r_result = dfs(node.right,target)
        #             if l_result is False or r_result is False:
        #                 return False
        #             else:
        #                 return True
        #     else:
        #         return True
        # target = root.val
        # result = dfs(root,target)
        # return result

        # method 2: recursion
        # 通过得到所有左边的结果，和所有右边的结果进行对比
        left_correct = (not root.left or root.val == root.left.val
                        and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                         and self.isUnivalTree(root.right))
        return left_correct and right_correct
