n = int(input())
dp = [list(map(int, input().split())) + [0] * (n-1-i) for i in range(n)]

for i in range(1, n):
    for j in range(0, i+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]
print(max(dp[n-1]))




