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
