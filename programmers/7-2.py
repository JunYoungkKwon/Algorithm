def solution(triangle):
    max_len = len(triangle)
    dp = [row[:] for row in triangle]

    for i in range(max_len - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    return (max(dp[max_len - 1]))


