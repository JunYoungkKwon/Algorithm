dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

R, C, K = map(int, input().split())
board = [input() for _ in range(R)]
chk = [[False] * C for _ in range(R)]
ans = 0


def is_valid_coord(y, x):
    return 0 <= y < R and 0 <= x < C


def backtracking(y, x, d):
    global ans
    if y == 0 and x == C - 1 and d == K:
        ans += 1
        return

    if d < K:
        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '.' and not chk[ny][nx]:
                chk[ny][nx] = True
                backtracking(ny, nx, nd)
                chk[ny][nx] = False


if board[R - 1][0] == 'T' or board[0][C - 1] == 'T':
    print(0)
else:
    chk[R - 1][0] = True
    backtracking(R - 1, 0, 1)
    chk[R - 1][0] = False

    print(ans)