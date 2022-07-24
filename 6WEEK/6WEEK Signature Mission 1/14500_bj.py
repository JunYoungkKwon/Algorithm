N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def tech(board,i,j,N,M):
    ans = 0
    if j+3 < M:
        ans = max(ans, sum(board[i][j:j+4]))
    if i+3 < N:
        number = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
        ans = max(ans, number)
    if j+1 < M and i+1 < N:
        number = board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1]
        ans = max(ans, number)
    if j+2 < M and i+1 < N:
        for k in range(3):
            number = sum(board[i][j:j + 3]) + board[i + 1][j + k]
            ans = max(ans, number)
        for k in range(3):
            number = sum(board[i + 1][j:j + 3]) + board[i][j + k]
            ans = max(ans, number)
    if j+1 < M and i+2 < N:
        for k in range(3):
            number = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + k][j + 1]
            ans = max(ans, number)
        for k in range(3):
            number = board[i][j+1] + board[i + 1][j + 1] + board[i + 2][j + 1] + board[i + k][j]
            ans = max(ans, number)
        for k in range(2):
            number = board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + (1-k)] + board[i][j+k]
            ans = max(ans, number)
    if j+2 < M and i+1 < N:
        number = board[i][j + 1] + board[i + 1][j + 1] + board[i][j] + board[i + 1][j + 2]
        ans = max(ans, number)
        number = board[i][j + 1] + board[i + 1][j + 1] + board[i+1][j] + board[i][j + 2]
        ans = max(ans, number)

    return ans


for i in range(N):
    for j in range(M):
        ans= max(ans,tech(board,i,j,N,M))
print(ans)
