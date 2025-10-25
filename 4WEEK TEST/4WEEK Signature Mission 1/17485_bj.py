# 우주선은 전에 움직인 방향으로 움직일 수 없다. 즉, 같은 방향으로 두번 연속으로 움직일 수 없다
#
# 방향은 3개
# j = 0, 1, 2
# dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i-1][j+1]
#
# dp[i][0] = dp[i-1][j] or dp[i-1][j+1]
# dp[i][1] = dp[i-1][j-1] or dp[i-1][j+1]
# dp[i][2] = min(dp[i-1][j], dp[i-1][j+1]) + board[i][j]
#
# N, M = map(int, input().rstrip().split())
# board = [list(map(int, input().rstrip().split())) for _ in range(N)]
# dp = [[0]*2 for _ in range(N)]
#
# for a in range(M):
#     dp[0][a] = board[0][a]
#
#
#
#
#
#
#
#
# print(min(dp[N-1]))