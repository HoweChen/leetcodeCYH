# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return [0]
        stack = [root]
        result = []
        while stack:
            count = len(stack)
            print(count)
            result.append(sum(x.val for x in stack[0:count])/count)
            new_stack = []
            for i in range(count):
                node = stack.pop()
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return result
                