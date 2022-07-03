from collections import deque

#동남서북
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    q = deque()
    q.append((0, 0, 1))
    print(q)
    while q:
        y, x, d = q.popleft()
        print(f'{y} {x} {d}')

        if y == N - 1 and x == M - 1:
            return d

        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx, nd))


print(bfs())