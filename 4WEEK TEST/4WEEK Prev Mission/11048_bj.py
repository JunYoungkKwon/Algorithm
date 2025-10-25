import sys

input = sys.stdin.readline

N, M = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] = (0,0)에서 (i,j)까지 올 수 있는 최대 사탕 합
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 왼쪽, 위, 대각선 왼쪽 위 중 최대값
        left = dp[i][j - 1] if j > 0 else 0
        up = dp[i - 1][j] if i > 0 else 0
        diag = dp[i - 1][j - 1] if i > 0 and j > 0 else 0

        dp[i][j] = max(left, up, diag) + candy[i][j]

print(dp[N - 1][M - 1])
