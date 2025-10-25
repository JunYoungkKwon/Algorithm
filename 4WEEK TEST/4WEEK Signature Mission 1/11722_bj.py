N = int(input())
dp = [1] * N
li = list(map(int, input().split()))

for i in range(N-1,-1, -1):
    for j in range(i+1, N):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))