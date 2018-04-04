class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_length = len(s)
        if s_length < 2:
            return s
        else:
            self.max_length = 0
            self.result = None
            for index in range(0, s_length-1):
                self.is_palindromic(s, index, index)
                self.is_palindromic(s, index, index+1)
            return self.result

    def is_palindromic(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # when it spread from middle to both sides, so in this case, left could be -1, that's why we need to use left+1
        if right-1-left > self.max_length:
            self.max_length = right-1-left
            self.result = s[left+1:right]


a = Solution()
# print(a.longestPalindrome('babad'))
# print(a.longestPalindrome('cbbd'))
print(a.longestPalindrome('abcda'))
print(a.longestPalindrome('cbbd'))
print(a.longestPalindrome('abbac'))
