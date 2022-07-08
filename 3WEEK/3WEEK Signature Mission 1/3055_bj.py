#최단 경로 bfs
#이미 익숙한 문제인데 예외처리... 집중해서 하자

from collections import deque


dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x):
    return 0 <= y < R and 0 <= x < C

def bfs():
    while q:
        y, x, d, m = q.popleft()

        if adj[y][x] == "D" and m == "start":
            print(d)
            return

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d + 1
            if is_valid_coord(ny, nx):
                if m == "water":
                    if chk[ny][nx] != 1 and (adj[ny][nx] == "." or adj[ny][nx] == "S"):
                        chk[ny][nx] = 1
                        q.append((ny, nx, nd, f))

                if m == "start":
                    if chk[ny][nx] == 0 and (adj[ny][nx] == "." or adj[ny][nx] == "D"):
                        chk[ny][nx] = 2
                        q.append((ny, nx, nd, s))

    return print("KAKTUS")


d= 0
s = "start"
f = "water"
e = "end"

R, C = map(int, input().split())
adj = [input().strip() for _ in range(R)]

chk = [[0] * C for _ in range(R)]
q = deque()
for i in range(R):
    for j in range(C):
        if is_valid_coord(i, j) and not chk[i][j]:
            if adj[i][j] == "S":
                chk[i][j] = True
                start = (i, j, d, s)
            if adj[i][j] == "*":
                chk[i][j] = 1
                q.append((i, j, d, f))

q.append(start)
bfs()
