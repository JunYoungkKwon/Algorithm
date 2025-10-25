import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

MOD = 1000000007

dp = [[0] * (M) for _ in range(N)]

for i in range(M):
    dp[0][i] = board[0][i]

#+1 할지 말지 고민
for i in range(1, N):
    for j in range(M):
        if board[i][j] == 1:
            if j == 0:
               dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j ==M-1:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]


sum = 0
for a in range(M):
    sum += dp[N-1][a]

print(sum % MOD)
