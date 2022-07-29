N = int(input())
board = [list(input()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def change_color(y, x, ny, nx):
    a = board[y][x]
    board[y][x] = board[ny][nx]
    board[ny][nx] = a


    return 0 <= y < N and 0 <= x < N
def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N
def fine_max():
    ans = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

        cnt = 1
        for j in range(1, N):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
    return ans

def dfs(y, x, d):
    global max_result
    global ans
    if d == 1:
        #행열에서 최대값 찾고 리턴
        ans = max(max_result, fine_max())
        return
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid(ny, nx):
            if board[y][x] != board[ny][nx]:
                change_color(y, x, ny, nx)
                #이렇게하면 0,0에서만 4방향을 돌고 d=1이라서 끝이난다 그냥 완전 탐색으로 해야 됨
                dfs(ny, nx, d+1)
                change_color(y, x, ny, nx)
max_result = 0
ans = 0
dfs(0, 0, 0)
print(ans)