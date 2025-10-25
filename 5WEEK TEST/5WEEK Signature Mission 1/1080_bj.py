N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = [list(input()) for _ in range(N)]

cnt = 0


#3*3 수정하기
def three_three(y, x):
    for i in range(y,y+3):
        for j in range(x, x + 3):
            if board[i][j] == "1":
                board[i][j] = "0"
            else:
                board[i][j] = "1"


for i in range(N-2):
    for j in range(M-2):
        if board[i][j] != ans[i][j]:
            three_three(i, j)
            cnt += 1

if board == ans:
    print(cnt)
else:
    print(-1)