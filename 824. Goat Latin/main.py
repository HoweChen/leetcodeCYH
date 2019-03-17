class Solution:
    def toGoatLatin(self, S: str) -> str:
        result = []
        for index, word in enumerate(S.split()):
            if word[0] in set("aeiouAEIOU"):
                word = word+"ma"
            else:
                word = word[1:]+word[0]+"ma"

            word += "a"*(index+1)

            result.append(word)
        result = " ".join(result)

        return result
