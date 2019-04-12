class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # method 1
        # intuition method
        # if numRows==0:return []
        # elif numRows==1:return [[1]]
        # else:
        #     result = [[1],[1,1]]
        #     if numRows == 2:
        #         return result
        #     else:
        #         for i in range(2,numRows):
        #             result.append([1])
        #             for j in range(1,i):
        #                 result[i].append(result[i-1][j-1] + result[i-1][j])
        #             result[i].append(1)
        #         return result

        # method 2:
        # 竖式计算，把上一行的数字右移一位，左边补0做计算
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]
