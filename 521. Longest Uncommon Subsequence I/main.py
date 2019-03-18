class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if not a and not b:
            return -1
        elif a == b:
            return -1
        else:
            return max(len(a), len(b))
