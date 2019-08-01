class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text = text.split()
        i=0
        result = []
        while i<len(text)-2:
            if text[i] == first and text[i+1] == second:
                result.append(text[i+2])
                i+=2
            else:
                i+=1
        return result