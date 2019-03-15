class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        counter = Counter((A+" "+B).split())
        result = []
        return [word for word in counter if counter[word] == 1]
