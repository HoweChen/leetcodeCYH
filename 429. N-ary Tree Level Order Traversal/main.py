"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None

        # bfs
        # from collections import deque
        # dq = deque()
        # dq.append(root)
        # result = []
        # while dq:
        #     cll = len(dq)  # current level length
        #     tmp_list = []
        #     for i in range(cll):
        #         node = dq.popleft()
        #         tmp_list.append(node.val)
        #         if node.children:
        #             for child in node.children:
        #                 dq.append(child)
        #     result.append(tmp_list)
        # return result

        # opTimized code
        stack, result = [root], []
        while stack:
            result.append([node.val for node in stack])
            stack = [child for node in stack for child in node.children if child]
        return result
