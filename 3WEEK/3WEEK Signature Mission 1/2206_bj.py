#2차원 배열로도 가능하지만 내 로직이 이상함
from collections import deque

N, M = map(int, input().split())

chk = [[0] * M for _ in range(N)]
adj = [list(map(int, input())) for _ in range(N)]

dy = [0,-1,0,1]
dx = [1,0,-1,0]

def is_valid_coord(y,x):
  return 0 <= y < N and 0 <= x < M


def bfs():
    q = deque()
    q.append((0,0,1,0))
    chk[0][0] = True

    while q:
        y, x, d, remove = q.popleft()
        # N,M에 도달시 최단 거리
        if y == N - 1 and x == M - 1:
            return print(d)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1

            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                if remove == 0:
                    if adj[ny][nx] == 1:
                        q.append((ny, nx, nd, 1))
                if adj[ny][nx] == 0:
                    chk[ny][nx] = True
                    q.append((ny, nx, nd, 0))


    return print(-1)

bfs()