def solution(money):
    n = len(money)

    # 예외 처리
    if n == 1:
        return money[0]

    # 1️⃣ 첫 집 포함 → 마지막 집 제외
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, n - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    # 2️⃣ 첫 집 제외 → 마지막 집 포함 가능
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    return max(dp1[n-2], dp2[n-1])
