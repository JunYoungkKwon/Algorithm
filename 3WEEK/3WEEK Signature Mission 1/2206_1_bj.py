from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    chk[0][0][0] = True
    q = deque()
    q.append((0, 0, 0, 1))

    while q:
        y, x, t, d = q.popleft()  # t가 0: 벽 부수기 미사용, 1: 벽 부수기 사용

        if y == N - 1 and x == M - 1:
            return d

        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx):
                nt = t
                if board[ny][nx] == '0' and not chk[ny][nx][nt]:
                    chk[ny][nx][nt] = True
                    q.append((ny, nx, nt, nd))

                if t == 0:
                    nt = t + 1
                    if board[ny][nx] == '1' and not chk[ny][nx][nt]:
                        chk[ny][nx][nt] = True
                        q.append((ny, nx, nt, nd))

    return -1


N, M = map(int, input().split())
board = [input() for _ in range(N)]
print(bfs())
