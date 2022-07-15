#이미 풀어 본 유형이라 그냥 바로 풀렸음
N = int(input())
li = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(100)]
dp[0][li[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if dp[i - 1][j]:

            if 0 <= j + li[i] <= 20:
                dp[i][j + li[i]] += dp[i - 1][j]

            if 0 <= j - li[i] <= 20:
                dp[i][j - li[i]] += dp[i - 1][j]
print(dp[N-2][li[-1]])