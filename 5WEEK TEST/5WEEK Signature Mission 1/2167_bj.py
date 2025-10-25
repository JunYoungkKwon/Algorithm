N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(int(input())):
    y, x, ny, nx = map(int, input().split())

    ans = 0
    if y == ny and x == nx:
        ans += board[y-1][x-1]

    elif y == ny and x != nx:
        for i in range(x-1, nx):
            ans += board[y-1][i]

    elif x == nx and y != ny:
        for i in range(y-1, ny):
            ans += board[i][x-1]

    else:
        for i in range(y-1, ny):
            for j in range(x-1, nx):
                ans += board[i][j]

    print(ans)