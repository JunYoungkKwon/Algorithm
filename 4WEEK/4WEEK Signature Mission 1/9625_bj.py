#문자열로 저장해서 출력하면 최적화를 해도 메모리 초과..
#어차피 문자열의 길이를 출력하는 것과 같으니 숫자로 값을 저장
K = int(input())
dp = [0] * 46

dp[0],dp[1] = 1, 1

for i in range(2, K+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[K-2], dp[K-1])