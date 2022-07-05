# 최단경로가 아니기 때문에 dfs 선택
def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def dfs(y, x, d):
    global cnt

    if x == M - 1 and y == N - 1 and d == K:
        cnt += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if is_valid_coord(ny, nx) and board[ny][nx] == "." and not chk[ny][nx]:
            chk[ny][nx] = True
            print(chk)
            print(f'{nx} {ny} {cnt}')
            dfs(ny, nx, d + 1)
            chk[ny][nx] = False
            print(f'{nx} {ny} {cnt} chk')
            print(f'{chk} chk')


N, M, K = map(int, input().split())
board = [input() for _ in range(N)]
board.reverse()

chk = [[False] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt = 0

chk[0][0] = True
dfs(0, 0, 1)
print(cnt)
