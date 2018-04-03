class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.max_length = 0
        self.sub_str_dict = {}
        self.result = ''
        s_length = len(s)
        for index in range(0, s_length):
            self.is_palindromic(s, index, index)
            self.is_palindromic(s, index, index+1)
        return max(self.sub_str_dict.keys(), key=lambda key: self.sub_str_dict[key])

    def is_palindromic(self, s, left, right):
        while left >= 0 and right < len(s):
            if left == right and s[left] not in self.sub_str_dict:
                self.sub_str_dict[s[left]] = len(s[left])
            elif right-left == 1 and s[left] == s[right]and s[left:right+1] not in self.sub_str_dict:
                self.sub_str_dict[s[left:right+1]] = len(s[left:right+1])
            else:
                if s[left+1:right] in self.sub_str_dict and s[left] == s[right]:
                    self.sub_str_dict[s[left:right+1]] = len(s[left:right+1])
            left -= 1
            right += 1


a = Solution()
# print(a.longestPalindrome('babad'))
# print(a.longestPalindrome('cbbd'))
print(a.longestPalindrome('abcda'))
