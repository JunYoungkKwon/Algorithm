# import sys
# input = sys.stdin.readline
#
# 작게 나눠보면
# 상담을 신청한다 or 안한다
#
# #신청을 안하면
# dp[i] = dp[i-1]
# #신청을 한다
# dp[i] = fee[i] + dp[i-1]
#
# N = int(input())
# period = []
# fee = []
# dp = [[0] * (N+2) for _ in range(2)]
#
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     period.append(a)
#     fee.append(b)
#
# dp[0][1] = fee[0]
#
# for i in range(1, N):
#     if period[i-1] == 1:
#
#     if period[i-1]
#     #신청을 한다
#
#
#
#
#     #신청을 안한다
#
