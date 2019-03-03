class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        size = 8
        row_index = None
        col_index = None
        for row in range(0, size):
            for col in range(0, size):
                if board[row][col] == "R":
                    row_index = row
                    col_index = col

        if row_index is None and col_index is None:
            return 0

        row_list = board[row_index]
        col_list = [board[row][col_index] for row in range(0, size)]
        # print(row_list)
        # print(col_list)

        result = 0

        # start from rol_list, the index is the col_index
        for col in range(col_index, size):
            if row_list[col] == "B":
                break
            else:
                if row_list[col] == "p":
                    result += 1
                    break

        for col in range(col_index, -1, -1):
            if row_list[col] == "B":
                break
            else:
                if row_list[col] == "p":
                    result += 1
                    break

        # col_list process,which row_index is the index
        for row in range(row_index, size):
            if col_list[row] == "B":
                break
            else:
                if col_list[row] == "p":
                    result += 1
                    break

        for row in range(row_index, -1, -1):
            if col_list[row] == "B":
                break
            else:
                if col_list[row] == "p":
                    result += 1
                    break

        # print(result)
        return result
