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
