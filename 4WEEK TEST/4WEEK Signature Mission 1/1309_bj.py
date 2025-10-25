# N = int(input())
# MOD = 1000000000
#
# dp = [[0]*3 for _ in range(N+1)]
#
# dp[1][0] = dp[1][1] = dp[1][2] = 1
#
# for i in range(2, N+1):
#     dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
#     dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
#     dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD
#
# print(sum(dp[N]) % MOD)


K = int(input())
MOD = 9901
MAX = 100000
dp = [0] * (MAX+1)
dp[1] = 3
dp[2] = 7

if K < 3:
    print(dp[K])
else:
    for i in range(3, K + 1):
        dp[i] = (dp[i - 2] + dp[i - 1] * 2) % MOD
    print(dp[K])