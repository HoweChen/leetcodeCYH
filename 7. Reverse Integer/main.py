import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
        x = str(abs(x))
        result = int(x[::-1])
        result = -result if negative else result
        if result < -2**31 or result > 2**31:
            return 0
        else:
            return result
