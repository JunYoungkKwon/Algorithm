# 간단한데 계속 이상하게 고민해서 오래 걸렸음..
K = int(input())
li = [0]
for _ in range(K):
    li.append(int(input()))
dp = [0] * (K+1)

if K == 1:
    print(li[1])
else:
    dp = [0] * (K + 1)
    dp[1], dp[2] = li[1], li[1] + li[2]

    for i in range(3, K + 1):
        dp[i] = max(li[i - 1] + dp[i - 3] + li[i], dp[i - 2] + li[i])
    print(dp[K])




