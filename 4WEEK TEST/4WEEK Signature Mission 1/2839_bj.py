N = intN = int(input())

dp = [5001] * (N + 1)   # 충분히 큰 수 (불가능 표시)
dp[0] = 0

for i in range(3, N + 1):
    if i >= 3:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[N] if dp[N] != 5001 else -1)
