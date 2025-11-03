# 첫째 줄에 시험장의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 각 시험장에 있는 응시자의 수 Ai (1 ≤ Ai ≤ 1,000,000)가 주어진다.
# 셋째 줄에는 B와 C가 주어진다. (1 ≤ B, C ≤ 1,000,000)
# 총감독 감시 B명 부감독 감시 C명
# 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 가능
# 감독관 수의 최솟값

import sys
input = sys.stdin.readline

N = int(input())
student = list(map(int, input().rstrip().split()))
B, C  = map(int, input().split())

dp = [0] * (max(student)+1)
sum = 0

for i in student:
    if dp[i] != 0:
        sum += dp[i]
    else:
        if i <= B:
            dp[i] = 1
            sum += 1
        else:
            one = 1
            a = i - B
            if a % C == 0:
                two = a // C
            else:
                two = (a // C) + 1
            total = one + two
            dp[i] = total
            sum += total

print(sum)

