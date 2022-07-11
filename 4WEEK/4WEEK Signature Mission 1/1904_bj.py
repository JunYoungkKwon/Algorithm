N = int(input())
MOD = 15746

if N < 3:
    dp = [0] * (3)
    dp[1], dp[2] = 1, 2
else:
    dp = [0] * (1000001)
    dp[1], dp[2] = 1, 2
    for i in range(3, N+1):
        dp[i] = (dp[i-1]  + dp[i-2]) % MOD

print(dp[N])








