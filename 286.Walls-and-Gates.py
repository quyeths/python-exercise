from typing import List
from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()
        distance = 0

        def addRooms(row, col):
            if (
                row < 0
                or row == ROWS
                or col < 0
                or col == COLS
                or (row, col) in visit
                or rooms[row][col] == -1
            ):
                return
            visit.add((row, col))
            q.append([row, col])

        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    q.append([row, col])
                    visit.add((row, col))
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                rooms[row][col] = distance
                addRooms(row + 1, col)
                addRooms(row - 1, col)
                addRooms(row, col + 1)
                addRooms(row, col - 1)
            distance += 1
