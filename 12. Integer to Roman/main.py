

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = int(num)
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        m = num//1000
        c = (num-(num//1000*1000))//100
        x = (num-(num//100*100))//10
        i = (num-(num//10*10))//1
        return M[m]+C[c]+X[x]+I[i]


sol = Solution()
print(sol.intToRoman(3999))
