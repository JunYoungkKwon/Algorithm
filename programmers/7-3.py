def solution(m, n, puddles):
    MOD = 1_000_000_007

    # DP 배열 생성 (n행 m열)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 물 웅덩이 표시
    for x, y in puddles:
        dp[y][x] = -1   # 이동 불가 표시

    # 시작점
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            if i == 1 and j == 1:
                continue

            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    return dp[n][m]
