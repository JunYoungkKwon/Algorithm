#3차원 배열로 풀려고 시도 but 내 생각을 코드로 구현하는 것 포기하고 참고함
# n, s, m = map(int, input().split())
# array = list(map(int, input().split()))
#
# dp = [[0] *(m+1) for _ in range(n+1)]
# dp[0][s] = 1
#
# for i in range(1, n+1):
#     for j in range(m+1):
#         if dp[i-1][j] ==0:
#             continue
#         if j - array[i-1]>=0:
#             dp[i][j- array[i-1]] = 1
#         if j + array[i-1]<=m:
#             dp[i][j+ array[i-1]] = 1
# result = -1
# for i in range(m,-1,-1):
#     if dp[n][i] == 1:
#         result= i
#         break
# print(result)

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

