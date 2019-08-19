# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        stack = [(root, 0, 0)]
        is_x_found = (False,None,None)
        is_y_found = (False,None,None)
        print(root)
        while stack:
            new_stack = []
            for node, breadth,parent in stack:
                if node.val == x:
                    is_x_found = (True,breadth,parent)
                if node.val == y:
                    is_y_found = (True,breadth,parent)
                if node.left:
                    new_stack.append((node.left,breadth+1,node.val))
                if node.right:
                    new_stack.append((node.right,breadth+1,node.val))
            stack = new_stack
        if is_x_found[0] and is_y_found[0]:
            if is_x_found[2] == is_y_found[2]:
                # found but same parent
                return False
            else:
                if is_x_found[1] == is_y_found[1]:
                    # found and same breadth but different parent
                    return True
        else:
            return False