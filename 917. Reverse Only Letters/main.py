class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # methood 1
        # 记录所有的单词
        #         import string
        #         str_list = []
        #         for char in S:
        #             if char in string.ascii_letters:
        #                 str_list.append(char)

        #         result = ""
        #         for index in range(len(S)):
        #             if S[index] in string.ascii_letters:
        #                 result+=str_list.pop()
        #             else:
        #                 result+=S[index]
        #         return result

        # method
        # bi-direction pointer 双端指针
        import string
        S = list(S)
        f_ptr = 0
        b_ptr = len(S)-1
        while f_ptr <= b_ptr:
            # print(f_ptr,b_ptr)
            if S[f_ptr] in string.ascii_letters:
                if S[b_ptr] in string.ascii_letters:
                    # print(S[f_ptr],S[b_ptr])
                    S[f_ptr], S[b_ptr] = S[b_ptr], S[f_ptr]
                    f_ptr += 1
                b_ptr -= 1
            else:
                if S[b_ptr] not in string.ascii_letters:
                    b_ptr -= 1
                f_ptr += 1

            # print("------")
        result = "".join(S)
        return result
