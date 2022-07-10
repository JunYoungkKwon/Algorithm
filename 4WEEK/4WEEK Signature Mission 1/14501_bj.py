N = int(input())

MOD = 10_007

dp = [0] * (N + 1)
dp[1] = 1
if N ==1:
    print(1)
else:
    dp[2] = 3
    for i in range(3, N + 1):
        if (i % 2) == 0:
            dp[i] = dp[i - 1] * 2 + 1
        else:
            dp[i] = dp[i - 1] * 2 - 1
    print(dp[N] % MOD)



