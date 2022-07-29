N = int(input())
board = [list(input()) for _ in range(N)]
check = [[0] * N for _ in range(N)]
#red = C, blue = P, green = Z, yellow = Y
color = [0] * 4
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
x, y = 0, 0
def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N
def color_chk(y, x, ny, nx):
    if board[y][x] == board[ny][nx]:
        return False
    else:
        return True
def change_color(y, x, ny, nx):
    a = board[y][x]
    board[y][x] = board[ny][nx]
    board[ny][nx] = a

def count_color():
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



result = 0
while True:
    if y == N:
        break
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid(ny, nx):
            # 1.상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
            if color_chk(y, x, ny, nx):
                # 2.그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
                change_color(y, x, ny, nx)
                # for i in range(N):
                #     print(*board[i])
                # print(f'result = {result}, x = {x},y = {y}, nx = {nx}, ny = {ny}')
                result = max(result, count_color())
                change_color(y, x, ny, nx)  # 원상복구

    if x < N-1:
        x = x + 1
    else:
        y = y + 1
        x = 0
print(result)