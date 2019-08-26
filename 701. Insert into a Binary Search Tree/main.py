# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 找到可以插入的地方放进原有树里
        # def insert(node,val,parent):
        #     if not node:
        #         new_node = TreeNode(val)
        #         if val < parent.val:
        #             parent.left = new_node
        #         else:
        #             parent.right = new_node
        #     else:
        #         if val < node.val:
        #             insert(node.left,val,node)
        #         else:
        #             insert(node.right,val,node)
        # if not root:
        #     return TreeNode(val)
        # else:
        #     insert(root,val,root)
        #     return root

        # 简化版
        # if(root == None): return TreeNode(val);
        # if(root.val < val): root.right = self.insertIntoBST(root.right, val);
        # else: root.left = self.insertIntoBST(root.left, val);
        # return(root)

        if not root:
            node = TreeNode(val)
            return node
        if val < root.val:
            if not root.left:
                # 这里直接处理可以减少一次递归
                node = TreeNode(val)
                root.left = node
            else:
                self.insertIntoBST(root.left, val)
        else:
            if not root.right:
                # 这里直接处理可以减少一次递归
                node = TreeNode(val)
                root.right = node
            else:
                self.insertIntoBST(root.right, val)
        return root
