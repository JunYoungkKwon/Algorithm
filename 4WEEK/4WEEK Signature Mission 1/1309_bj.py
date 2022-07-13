#3차원 배열로 풀려고 시도 but 내 생각을 코드로 구현하는 것 포기하고 참고함
n, s, m = map(int, input().split())
array = list(map(int, input().split()))

dp = [[0] *(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] ==0:
            continue
        if j - array[i-1]>=0:
            dp[i][j- array[i-1]] = 1
        if j + array[i-1]<=m:
            dp[i][j+ array[i-1]] = 1
result = -1
for i in range(m,-1,-1):
    if dp[n][i] == 1:
        result= i
        break
print(result)

# N, S, M = map(int, input().split())
# li = list(map(int, input().split()))
# dp = [[[0] * 2500 for _ in range(2500)] for _ in range(2)]
# dp[0][0][0] = S
# for i in range(1, 2500):
#     for j in range(0, len(dp[i])):
#         p = dp[i - 1][j][j] + li[0]
#         m = dp[i - 1][j][j] - li[0]
#         if 0 <= p <= M:
#             dp[i][j][0] = p
#         if 0 <= m <= M:
#             dp[i][j][1] = m

