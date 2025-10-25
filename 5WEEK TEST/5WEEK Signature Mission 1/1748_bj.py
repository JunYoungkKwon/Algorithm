dp = [0] * 10
dp[1] = 9
dp[2] = 90 * 2
dp[3] = 900 * 3
dp[4] = 9000 * 4
dp[5] = 90000 * 5
dp[6] = 900000 * 6
dp[7] = 9000000 * 7
dp[8] = 90000000 * 8
dp[9] = 900000000 * 9

N = int(input())
le = len(str(N))
ans = 0
for i in range(le):
    ans += dp[i]

ans_2 = ((N-(10**(le-1)))+1) * le

print(ans+ans_2)



