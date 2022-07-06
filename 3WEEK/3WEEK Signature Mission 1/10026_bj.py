from collections import deque

N = int(input())
adj = [list(input()) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

def is_valid_coord(y, x):
    return 0 <= x < N and 0 <= y < N

def bfs(y, x):
    q = deque()
    q.append((y, x))
    chk[y][x] = True
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx] and adj[y][x] == adj[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx))


cnt = 0
for i in range(N):
    for j in range(N):
        if is_valid_coord(i, j) and not chk[i][j]:
            chk[i][j] = True
            bfs(i, j)
            cnt += 1

for i in range(N):
    for j in range(N):
        if adj[i][j] == "R":
            adj[i][j] = "G"

chk = [[False] * N for _ in range(N)]

cnt2 = 0
for i in range(N):
    for j in range(N):
        if is_valid_coord(i, j) and not chk[i][j]:
            chk[i][j] = True
            bfs(i, j)
            cnt2 += 1

print(cnt, cnt2)