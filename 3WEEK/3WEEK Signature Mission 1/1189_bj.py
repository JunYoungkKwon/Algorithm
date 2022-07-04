def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


def dfs(y, x, d):
    global cnt
    chk[y][x] = True
    if x == M - 1 and y == N - 1 and d == K:
        cnt += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if is_valid_coord(ny, nx) and board[ny][nx] == "." and not chk[ny][nx]:
            dfs(ny, nx, d + 1)


N, M, K = map(int, input().split())
board = [input() for _ in range(N)]
board.reverse()

chk = [[False] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt = 0

dfs(0, 0, 1)
print(cnt)
