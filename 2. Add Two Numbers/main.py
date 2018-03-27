# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_number = self.get_number(l1)
        second_number = self.get_number(l2)
        adition_result = str(first_number + second_number)
        ListNode_list = []
        for char in adition_result[::-1]:
            tmp = ListNode(int(char))
            ListNode_list.append(tmp)

        for index in range(0, len(ListNode_list)-1):
            ListNode_list[index].next = ListNode_list[index+1]
        return ListNode_list[0]

    def get_number(self, input_list_node):
        result = ''
        while(input_list_node):
            result += str(input_list_node.val)
            input_list_node = input_list_node.next
        return int(result[::-1])
