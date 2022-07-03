from collections import deque
import sys
input = sys.stdin.readline

# 동남서북
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

res = 0
li = []

N, M, K = map(int, input().split())
adj = [[0] * M for _ in range(N)]
chk = [[False] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1 , y2):
        for j in range(x1, x2):
            adj[i][j] = 1

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs(x, y):
    cnt = 1
    chk[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        y, x= q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and adj[ny][nx] == 0 and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx))
                cnt += 1
    return cnt

for i in range(N):
    for j in range(M):
        if adj[i][j] == 0 and not chk[i][j]:
            li.append(bfs(i, j))

li = sorted(li)
print(len(li))
print(*li)