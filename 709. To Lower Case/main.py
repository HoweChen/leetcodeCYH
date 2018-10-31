class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        if str:
            return str.lower()
        elif str == "":
            return ""
        else:
            return None


sol = Solution()

print(sol.toLowerCase("Fuck"))
print(sol.toLowerCase(123))
print(sol.toLowerCase("LOVELY"))
