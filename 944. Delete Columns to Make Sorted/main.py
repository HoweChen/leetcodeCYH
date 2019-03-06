class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        # method 1:
        # 思路是遍历所有的列，如果sorted之后和原来的相同则保留，否则增加计数
        #         result = 0
        #         if A:
        #             col_len=len(A)
        #             str_len = len(A[0])
        #             new_list = [[] for i in range(str_len)]
        #             for col in range(str_len):
        #                 for row in range(col_len):
        #                     new_list[col].append(A[row][col])

        #             for sub_list in new_list:
        #                 if sub_list:
        #                     if sub_list != sorted(sub_list):
        #                         result+=1
        #                 else:
        #                     continue
        #         return result

        # method 1 更快的方法： 利用 zip(*a)
        zipped = zip(*A)
        ans = 0
        for z in zipped:
            z = list(z)
            if z != sorted(z):
                ans += 1
        return ans
