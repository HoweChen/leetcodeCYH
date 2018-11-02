class Solution:

    @staticmethod
    def revert_num(input_num):
        if input_num == 1:
            return 0
        if input_num == 0:
            return 1
        else:
            return None

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for singleList in A:
            if singleList:
                # flag = len(singleList) % 2
                # mid = len(singleList)//2
                # singleResult = []
                # if flag == 0:
                #     # even number of elements in that list
                #     for index in range(len(singleList)-1, mid-1, -1):
                #         singleResult.append(
                #             Solution.revert_num(singleList[index]))
                # else:
                #     # odd number of elements in that list
                #     for index in range(mid, 0, -1):
                #         singleResult.append(
                #             Solution.revert_num(singleList[index]))
                singleResult = list(reversed(singleList))
                for index in range(len(singleResult)):
                    singleResult[index] = Solution.revert_num(
                        singleResult[index])
                result.append(singleResult)
            else:
                return None
        return result


sol = Solution()
A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
B = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
C = [[1], [0], [0], [1]]
D = [[], [], [], []]
print(sol.flipAndInvertImage(A))
print(sol.flipAndInvertImage(B))
print(sol.flipAndInvertImage(C))
print(sol.flipAndInvertImage(D))
