class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        S_len = len(S)
        num_list = list(range(0, S_len+1))
        i_count = S.count("I")
        i = num_list[0:i_count]
        d = num_list[i_count::]
        i.reverse()
        # print(i,d)
        result = []
        for char in S:
            if char is "I" and i:
                result.append(i.pop())
            elif char is "D" and d:
                result.append(d.pop())

        while i:
            result.append(i.pop())

        while d:
            result.append(d.pop())

        # print(result)
        return result
