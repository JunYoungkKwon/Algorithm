K = int(input())
dp = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    for j in range(1, 31):
        if i == j:
            dp[i][j] = 1
        elif i == 1:
            dp[i][j] = j
        elif i > 1 and i < j:
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

for _ in range(K):
    N, M = map(int,input().split())
    print(dp[N][M])



