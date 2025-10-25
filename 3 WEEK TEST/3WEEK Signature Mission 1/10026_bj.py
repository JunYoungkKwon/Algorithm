import sys
from collections import deque

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(i, j):
    deq =deque()
    deq.append((i, j))
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid(ny, nx) and not visited[ny][nx]:
                if board[y][x] == board[ny][nx]:
                    visited[ny][nx] = True
                    deq.append((ny, nx))


cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
            cnt += 1

print(cnt)



