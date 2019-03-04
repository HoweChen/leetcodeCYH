class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        length = len(A)
        if length == 0 or length == 1:
            return A
        else:
            flag = list(A[0])
            comp_lists = [list(x) for x in A[1::]]
            for comp_list in comp_lists:
                index = 0
                while index < len(flag):
                    # print(flag)
                    # print(comp_list,index,flag[index])
                    if flag[index] in comp_list:
                        comp_list.remove(flag[index])
                        index += 1
                    else:
                        flag.remove(flag[index])

            # print(flag)
            return flag
