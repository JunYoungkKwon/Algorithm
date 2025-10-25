dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for l in range(21):
            if i <= 0 or j <= 0 or l <= 0:
                dp[i][j][l] = 1
            elif i < j and j < l:
                dp[i][j][l] =  dp[i][j][l-1]+dp[i][j-1][l-1]-dp[i][j-1][l]
            else:
                dp[i][j][l] = dp[i-1][j][l] + dp[i-1][j - 1][l] + dp[i-1][j][l-1]-dp[i-1][j-1][l-1]
                # 011 001 010 000
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = 1')

    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = 1048576')
    elif a < b and b < c:
        print(f'w({a}, {b}, {c}) = {dp[a][b][c-1]+dp[a][b-1][c-1]-dp[a][b-1][c]}')
    else:
        print(f'w({a}, {b}, {c}) = {dp[a-1][b][c] + dp[a-1][b - 1][c] + dp[a-1][b][c-1]-dp[a-1][b-1][c-1]}')
