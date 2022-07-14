num = [0] + list(input())
MOD = 1000000
if num[1] == '0':
    print(0)
    exit(0)

dp = [0] * len(num)
dp[0] = dp[1] = 1

for i in range(2, len(num)):
    first = int(num[i])
    tenth = int(num[i-1])*10 + int(num[i])
    if first > 0: dp[i] += dp[i-1]
    if tenth >= 10 and tenth <= 26: dp[i] += dp[i-2]

print(dp[-1] % MOD)