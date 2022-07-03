from collections import deque
import sys
input = sys.stdin.readline

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

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
            if is_valid_coord(ny, nx) and adj[ny][nx] == "1" and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx))
                cnt += 1
    return cnt


# 동남서북
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

res = 0
li = []

N = int(input())
adj = [input() for _ in range(N)]

chk = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if adj[i][j] == "1" and not chk[i][j]:
            li.append(bfs(i, j))

li = sorted(li)
print(len(li))
for i in range(len(li)):
    print(li[i])