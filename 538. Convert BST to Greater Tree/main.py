# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def convertBST(self, root: TreeNode)-> TreeNode:
        # use dfs to calculate the sum, very slow
        # def dfs(root,lst,cal=False):
        #     if root:
        #         if not cal:
        #             lst.append(root.val)
        #         else:
        #             root.val = sum(lst[lst.index(root.val)::])
        #         dfs(root.left,lst,cal)
        #         dfs(root.right,lst,cal)
        # if not root:
        #     return None
        # lst = []
        # dfs(root,lst)
        # lst = sorted(lst)
        # dfs(root,lst,True)
        # return root

        # from root.right to root.left
        # 先从树的最右边开始便利，因为右>根>左，所以左+=(根+右)，根+=右
        def dfs(root):
            if not root:
                return 0
            dfs(root.right)
            root.val += self.sum
            self.sum = root.val
            dfs(root.left)
        self.sum = 0
        dfs(root)
        return root
