class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack_list = []
        max_length = 0
        for i in range(0, len(s)):
            if s[i] not in stack_list:
                stack_list.append(s[i])
            else:
                if len(stack_list) > max_length:
                    max_length = len(stack_list)
                stack_list = stack_list[stack_list.index(s[i])+1:]
                stack_list.append(s[i])
        if len(stack_list) > max_length:
            max_length = len(stack_list)
        return max_length
