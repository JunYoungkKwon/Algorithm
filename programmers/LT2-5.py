# [리트코드] Shortest Path in Binary Matrix
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # ❗ 시작 / 끝 막혀 있으면 불가능
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        dx = [0, 0, -1, 1, 1, 1, -1, -1]
        dy = [-1, 1, 0, 0, -1, 1, -1, 1]

        visited = [[False] * n for _ in range(n)]
        deq = deque()
        deq.append((0, 0, 1))   # 거리 1부터 시작
        visited[0][0] = True

        while deq:
            y, x, dist = deq.popleft()

            if y == n - 1 and x == n - 1:
                return dist

            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if not visited[ny][nx] and grid[ny][nx] == 0:
                        visited[ny][nx] = True
                        deq.append((ny, nx, dist + 1))

        return -1