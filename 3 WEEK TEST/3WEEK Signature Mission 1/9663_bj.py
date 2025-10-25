dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

N = int(input())
ans = 0

def is_vaild(y,x ):
    return 0 <= y < N and 0 <= x < N

def backtracking(y, x, a):
    global ans
    ans = a
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_vaild(ny, nx) and not board[ny][nx]:
            board[ny][nx] = 1
            backtracking(ny, nx, a+1)
            board[ny][nx] = 0



board = [[0] * N for _ in range(N)]


for i in range(N):
    for j in range(N):
        board[i][j] = 1
        backtracking(i, j, 0)
        board[i][j] = 0

print(ans)

# N = int(input())
# ans = 0
#
# # 열, 좌대각, 우대각 체크
# col_check = [False] * N
# diag1_check = [False] * (2*N - 1)  # row + col
# diag2_check = [False] * (2*N - 1)  # row - col + (N-1)
#
# def backtracking(row):
#     global ans
#     if row == N:
#         ans += 1
#         return
#
#     for col in range(N):
#         if not col_check[col] and not diag1_check[row + col] and not diag2_check[row - col + N - 1]:
#             # 퀸 놓기
#             col_check[col] = True
#             diag1_check[row + col] = True
#             diag2_check[row - col + N - 1] = True
#
#             backtracking(row + 1)
#
#             # 원복
#             col_check[col] = False
#             diag1_check[row + col] = False
#             diag2_check[row - col + N - 1] = False
#
# backtracking(0)
# print(ans)


