0+4, 1+3, 2+2, 3+1, 4+0

n = 4 K=2
4를 2가지로
DP[2][4] = DP[1][4] + DP[2][3]


for i in range(2, 3):
    for j in range(1, 5):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        i=2
        j=1~4
        dp21 = dp11 + dp20

