class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top_max = len(
            [number for sub_list in grid for number in sub_list if number != 0])
        side_max = sum([max(sub_list) for sub_list in grid])
        # column_list = []
        # temp_list = []
        # for number in range(len(grid[0])):
        #     temp_list.clear()
        #     for sub_list in grid:
        #         temp_list.append(sub_list[number])
        #     column_list.append(max(temp_list))
        # front_max = sum(column_list)
        front_max = sum([max(i) for i in zip(*grid)])
        # print(grid)
        # print(top_max, side_max, front_max)
        return top_max+side_max+front_max


sol = Solution()

A = [[2]]
B = [[1, 2], [3, 4]]
C = [[1, 0], [0, 2]]
D = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
E = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
F = [[1, 0], [5, 4]]

A_sol = 5
B_sol = 17
C_sol = 8
D_sol = 14
E_sol = 21
F_sol = 18

print(sol.projectionArea(A))
print(sol.projectionArea(B))
print(sol.projectionArea(C))
print(sol.projectionArea(D))
print(sol.projectionArea(E))
print(sol.projectionArea(F))

assert sol.projectionArea(A) == A_sol
assert sol.projectionArea(B) == B_sol
assert sol.projectionArea(C) == C_sol
assert sol.projectionArea(D) == D_sol
assert sol.projectionArea(E) == E_sol
assert sol.projectionArea(F) == F_sol
