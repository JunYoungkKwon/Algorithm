
N = int(input())


dp = [0] * 32
dp[1] = 1
dp[2] = 2
for i in range(3, 31):
    dp[i] = dp[i-1] * i

for i in range(N):
    a, b = map(int, input().split())
    if a==b or a> b:
        print(1)
    else:
       ans = dp[b] // (dp[b-a] * dp[a])
       print(ans)