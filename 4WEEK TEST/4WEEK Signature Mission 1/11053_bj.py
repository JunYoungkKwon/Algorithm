n = int(input())
A = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


# A = [10, 20, 10, 30, 20, 50]
# dp = [1, 2, 1, 3, 1, 1]
# dp[i] = max(dp[j] + 1)    (단, j < i 이고 A[j] < A[i])