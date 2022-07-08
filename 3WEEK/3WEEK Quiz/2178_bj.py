from collections import deque
import sys

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    q = deque()
    q.append((0, 0, 1))

    while q:
        y, x, d = q.popleft()
        if y == N-1 and x == M-1:
            print(d)
            return

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d + 1
            if is_valid_coord(ny, nx) and not chk[ny][nx] and adj[ny][nx] == "1":
                chk[ny][nx] = True
                q.append((ny, nx, nd))

    return
d= 1

N, M = map(int, input().split())

adj = [input() for _ in range(N)]
chk = [[False] * M for _ in range(N)]
q = deque()

bfs()



