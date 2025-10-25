#어떻게 점화식을 짜야 할 지 몰라서 참고했음
N = int(input())

t = []
p = []
dp = [0] * (N+1)
for i in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)
for i in range(N-1, -1, -1):
    if i + t[i]> N:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 값 비교
        # i일에 상담을 하면 (i일 상담 비용 + i일 상담 끝나곤 난 이후 가능한 비용)
        # i일에 상담을 안하면 그 다음 날 이후의 총 상담비용 가져 옴
        dp[i] = max(dp[i+1], p[i] + dp[t[i] + i])
print(dp[0])


# 1  2  3  4  5  6  7일
# 3  5  1  1  2  4  2
# 10 20 10 20 15 40 200






