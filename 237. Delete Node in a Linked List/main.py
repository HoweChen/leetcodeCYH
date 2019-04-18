# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # method 1:
        # 把当前的这个node的值，换成下一个的
        # 把当前的node，指向到下一个的下一个，相当于值是下一个的，但是引用是下两个的
        # 把下一个的node给架空掉
        node.val = node.next.val
        node.next = node.next.next
