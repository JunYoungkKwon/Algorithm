#5의 배수 3의 배수일 때 나눠서 하는 경우가 직관적으로 떠올랐지만
#dp를 연습하기 위해서 dp 방식대로 고민 했고 규칙을 못 찾아서 참고했음 ㅠ
N = int(input())
dp = [2000] * 5001
dp[3], dp[5] = 1, 1
for i in range(6, 5001):
    dp[i] = min(dp[i-3], dp[i-5]) + 1


print(dp[N] if dp[N] < 2000 else -1)