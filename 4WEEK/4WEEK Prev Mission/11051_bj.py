#재귀 함수 도는데 pyp3에서 재귀함수 한도까지 많이 늘리면 메모리 초과남
# 한도를 적당히 늘려야 할 듯 10**5 정도??
MOD = 10007
cache = [[0] * 1001 for _ in range(1001)]

def dp(N , K):
    if cache[N][K] == 0:
        if K == 0 or N==K:
            cache[N][K] = 1
        else:
            cache[N][K] = (dp(N-1, K-1) + dp(N-1, K))

    return cache[N][K]


N, K = map(int, input().split())
print(dp(N, K) % MOD)