# 1 1
# 2 2
# 3 4 12 21 111 3
# 4 7 1111,22,211,112,121,31,13,
# 5 13 11111, 32, 23, 1112,2111,1211,1121, 212,122,221,113,311,131
# 6 24
# 7 44
# 8
# 9
# 10 274
import sys
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수

dp = [0] * 11  # n은 10 이하
dp[1], dp[2], dp[3] = 1, 2, 4

# 점화식 기반 DP 테이블 채우기
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 각 테스트 케이스 출력
for _ in range(T):
    n = int(input())
    print(dp[n])
