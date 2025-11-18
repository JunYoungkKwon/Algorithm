N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

ans = 0


def dfs(y, x, depth, hap):
    global ans
    if depth == 4:
        ans = max(ans, hap)
        return

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, depth + 1, hap + board[ny][nx])
            visited[ny][nx] = False


def check_extra(y, x):
    global ans
    # ㅗ, ㅏ, ㅜ, ㅓ 모양
    shapes = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
        [(0, 0), (0, 1), (0, 2), (-1, 1)],  # ㅗ
        [(0, 0), (1, 0), (2, 0), (1, -1)]  # ㅓ
    ]
    for shape in shapes:
        hap = 0
        ok = True
        for dy, dx in shape:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < M):
                ok = False
                break
            hap += board[ny][nx]
        if ok:
            ans = max(ans, hap)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_extra(i, j)

print(ans)
