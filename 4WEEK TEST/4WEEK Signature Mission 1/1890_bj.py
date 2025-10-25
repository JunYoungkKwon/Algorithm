# import sys
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0]*N for _ in range(N)]
#
# def is_valid(y, x):
#     return 0<= y < N and 0<= x < N
#
# dp[0][0] = 1  # 경로 수 1로 시작
#
# ans = 0
# for i in range(N):
#     for j in range(N):
#         if dp[i][j] == 0:  # 도달할 수 없는 칸은 무시
#             continue
#
#         jump = board[i][j]
#         # 오른쪽 점프
#         if is_valid(i, j+jump):
#             dp[i][j+jump] += dp[i][j]
#         # 아래 점프
#         if is_valid(i+jump, j):
#             dp[i+jump][j] += dp[i][j]
#
# print(dp[N-1][N-1])
