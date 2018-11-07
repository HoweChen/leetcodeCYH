"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # recursive

        if not root:
            return []
        traversal = [root.val]
        for child in root.children:
            traversal.extend(self.preorder(child))
        return traversal

        # # iterative
        # if not root:
        #     return []
        # traversal = []
        # stack = [root]
        # while stack:
        #     cur = stack.pop()
        #     traversal.append(cur.val)
        #     stack.extend(reversed(cur.children))
        # return traversal
