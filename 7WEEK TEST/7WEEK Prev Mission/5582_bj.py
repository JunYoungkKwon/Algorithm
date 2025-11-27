A = input().rstrip()
B = input().rstrip()

lenA = len(A)
lenB = len(B)

dp = [0] * (lenB + 1)
answer = 0

for i in range(1, lenA + 1):
    new_dp = [0] * (lenB + 1)
    for j in range(1, lenB + 1):
        if A[i-1] == B[j-1]:
            new_dp[j] = dp[j-1] + 1
            answer = max(answer, new_dp[j])
    dp = new_dp

print(answer)

A = input().rstrip()
B = input().rstrip()

la, lb = len(A), len(B)
answer = 0

# B를 A의 왼쪽으로 슬라이딩 이동
for shift in range(-lb+1, la):
    count = 0
    for i in range(lb):
        a_idx = shift + i
        if 0 <= a_idx < la:
            if A[a_idx] == B[i]:
                count += 1
                answer = max(answer, count)
            else:
                count = 0  # 연속이 끊기면 초기화
print(answer)

