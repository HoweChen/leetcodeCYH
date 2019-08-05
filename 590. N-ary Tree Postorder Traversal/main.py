"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # recursion
#         def recursion(node,res):
#             for child in node.children:
#                 recursion(child,res)
#             res.append(node.val)
        
#         result = []
#         if not root:
#             return None
#         else:
#             recursion(root,result)
#             return result
        # iteration
        res = []
        if root == None: return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)

        return res[::-1]