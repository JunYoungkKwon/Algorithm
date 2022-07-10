N, M = map(int, input().split())
MOD = 1000000007
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

for i in range(M):
    dp[N-1][i] = board[N-1][i]

for i in range(N-2, -1, -1):
    for j in range(M):
        if board[i][j] ==1:
            dp[i][j] = dp[i + 1][j]
            if j == 0:
                dp[i][j] += dp[i + 1][j + 1]
            elif j == M - 1:
                dp[i][j] += dp[i + 1][j - 1]
            else:
                dp[i][j] += (dp[i + 1][j - 1] + dp[i + 1][j + 1])

print(sum(dp[0]) % MOD)

