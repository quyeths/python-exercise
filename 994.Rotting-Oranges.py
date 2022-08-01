from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    row, col = row + dr, col + dc
                    if (
                        row in range(ROWS)
                        and col in range(COLS)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
