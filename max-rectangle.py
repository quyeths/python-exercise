from typing import List

board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


class Solution:
    def findMaxRectangle(self, board: List[List[int]], k: int) -> List[List[int]]:
        if not board:
            return

        ROWS, COLS = len(board), len(board[0])

        if k > ROWS or k > COLS:
            return

        self.max = 0
        result = [[0] * k for _ in range(k)]
        hashmap = {}
        index = 0

        def dfs(row, col):
            if row + k > ROWS or col + k > COLS:
                return 0
            sum = 0
            temp = []
            for r in range(row, row + k):
                for c in range(col, col + k):
                    sum += board[r][c]
                    temp.append(board[r][c])
            hashmap[sum] = temp
            return sum

        for row in range(ROWS):
            for col in range(COLS):
                self.max = max(self.max, dfs(row, col))
        for row in range(k):
            for col in range(k):
                result[row][col] = hashmap[self.max][index]
                index += 1
        return result
