class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_substring = ''
        max_length = 1
        if len(s) < 2:
            return s
        else:
            for i in range(0, len(s)):
                for j in range(i, len(s)-1):
                    if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > max_length:
                        max_substring = s[i:j+1]
                        max_length = len(max_substring)
            return max_substring
