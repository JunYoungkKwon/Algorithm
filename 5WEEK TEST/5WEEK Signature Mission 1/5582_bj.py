A = input().strip()
B = input().strip()


a_set = set()
b_set = set()

for size  in range(1, len(A)+1): # 부분 문자열 길이 (1 ~ len(A))
    for i in range(len(A) - size + 1):  # 시작 인덱스
        a_set.add(A[i:i + size])

for size  in range(1, len(B)+1): # 부분 문자열 길이 (1 ~ len(B))
    for i in range(len(B) - size + 1):  # 시작 인덱스
        b_set.add(B[i:i + size])

c = sorted(list(a_set & b_set))
max_len = max(len(s) for s in c) if c else 0

print(max_len)

A = input().strip()
B = input().strip()

# DP 테이블 (0으로 초기화)
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
ans = 0

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])  # 최대값 갱신

print(ans)
