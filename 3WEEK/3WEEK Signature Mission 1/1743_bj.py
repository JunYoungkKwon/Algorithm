from collections import deque
import sys
input = sys.stdin.readline

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
            if is_valid_coord(ny, nx) and adj[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx))
                cnt += 1
    return cnt


# 동남서북
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

res = 0

N, M, K = map(int, input().split())
adj = [[0] * M for _ in range(N)]
chk = [[False] * M for _ in range(N)]

ans = 0

for _ in range(K):
    #제로 베이스
    u, v = map(lambda x: x - 1, map(int, input().split()))
    adj[u][v] = 1

for i in range(N):
    for j in range(M):
        if adj[i][j] == 1 and not chk[i][j]:
            res = max(res, bfs(i, j))

print(res)

