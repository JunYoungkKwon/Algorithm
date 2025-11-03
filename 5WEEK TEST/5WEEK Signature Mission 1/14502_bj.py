import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

def bfs():
    global ans
    tmp = [row[:] for row in board]  # 깊은 복사
    q = deque()

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    q.append((nx, ny))


    safe = sum(row.count(0) for row in tmp)
    ans = max(ans, safe)


def dfs(count):
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(count + 1)
                board[i][j] = 0

dfs(0)
print(ans)
