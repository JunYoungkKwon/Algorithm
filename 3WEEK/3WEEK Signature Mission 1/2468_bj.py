from collections import deque
import sys

input = sys.stdin.readline


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


def bfs(x, y, hei):
    chk[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and adj[ny][nx] >= hei and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx))

# 동남서북
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
hei_max = max(map(max, adj))
hei_min = min(map(min, adj))
ans = []

for hei in range(hei_min, hei_max+1):
    chk = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if adj[i][j] >= hei and not chk[i][j]:
                bfs(i, j, hei)
                cnt += 1
    ans.append(cnt)
print(max(ans))