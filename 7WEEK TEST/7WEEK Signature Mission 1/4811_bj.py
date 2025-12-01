import sys
sys.setrecursionlimit(10000)
from functools import lru_cache

@lru_cache(None)
def dp(a, b):
    # a: 남은 정제 수
    # b: 남은 반쪽 수
    if a == 0 and b == 0:
        return 1
    res = 0
    if a > 0:
        res += dp(a-1, b+1)
    if b > 0:
        res += dp(a, b-1)
    return res

while True:
    N = int(input())
    if N == 0:
        break
    print(dp(N,0))

