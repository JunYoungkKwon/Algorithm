def solution(N, number):
    # dp[i]: N을 i번 사용해서 만들 수 있는 수의 집합
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # 이어붙이기 (예: 5, 55, 555)
        dp[i].add(int(str(N) * i))
        print(dp[i])

        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    print(dp[i])
                    if b != 0:
                        dp[i].add(a // b)

        # 목표 숫자 발견
        if number in dp[i]:
            return i

    return -1
solution(5,12)
