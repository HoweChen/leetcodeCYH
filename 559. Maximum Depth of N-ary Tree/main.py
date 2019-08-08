"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # dfs
        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            depth = 0
            for child in root.children:
                depth = max(depth,self.maxDepth(child))
            return depth+1
        
        # bfs
        # if not root:
        #     return 0
        # else:
        #     dq = deque()
        #     dq.append(root)
        #     depth = 0
        #     while len(dq) >0:
        #         depth+=1
        #         breadth = len(dq)
        #         for _ in range(breadth):
        #             node = dq.popleft()
        #             if node.children:
        #                 for child in node.children:
        #                     dq.append(child)
        #     return depth