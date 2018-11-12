# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.val:
            return None
        else:
            result_list = []
            while head.next:
                result_list.append(head)
                head = head.next
            result_list.append(head)

            if len(result_list) == 1:
                return result_list[0]
            else:
                return result_list[len(result_list)//2]


sol = Solution()
