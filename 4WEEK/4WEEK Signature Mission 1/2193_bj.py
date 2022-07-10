N = int(input())

dp = [0] * (101)
dp[1],dp[2],dp[3],dp[4],dp[5], = 1,1,1,2,2

for i in range(6, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(N):
    T = int(input())
    print(dp[T])