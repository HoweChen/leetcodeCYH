class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # method 1
        #         top_view_list = []
        #         left_view_list = []
        #         length = len(grid)

        #         for c in range(0,length):
        #             left_view_list.append(max(grid[c]))
        #             tmp = []
        #             for r in range(0,length):
        #                 tmp.append(grid[r][c])
        #             top_view_list.append(max(tmp))

        #         #print(top_view_list)
        #         #print(left_view_list)

        #         result = 0
        #         for r_index in range(0,length):
        #             for c_index in range(0,length):
        #                 num = grid[r_index][c_index]
        #                 top_most = top_view_list[c_index]
        #                 left_most = left_view_list[r_index]
        #                 min_threshold = min(top_most,left_most)
        #                 max_threshold = max(top_most,left_most)
        #                 if num < min_threshold:
        #                     result += min_threshold - num
        #                 if num in range(min_threshold+1,max_threshold-1):
        #                     result += max_threshold - num
        #         #print(result)
        #         return result

        # method 2
        l2r_skyline = list(map(max, grid))
        u2d_skyline = list(map(max, *grid))
        return sum(min(i, j) for i in l2r_skyline for j in u2d_skyline) - sum(map(sum, grid))
