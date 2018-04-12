class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if not s:
            return 0
        elif len(s) == 1:
            return roman_dict.get(s)
        else:
            current = roman_dict.get(s[0])
            result = 0
            for char in s[1::]:
                temp = roman_dict.get(char)
                if temp == current:
                    current += temp
                elif temp < current:
                    result += current
                    current = temp
                else:
                    current = temp-current
            result += current
            return result


sol = Solution()
print(sol.romanToInt('MMMCMXCIX'))
