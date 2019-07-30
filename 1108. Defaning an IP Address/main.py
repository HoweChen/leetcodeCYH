class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        cache = []
        for char in address:
            if char !=".":
                cache.append(char)
            else:
                new = "".join(cache)+"[.]"
                cache.clear()
                result +=new
        if cache:
            result += "".join(cache)
        return result