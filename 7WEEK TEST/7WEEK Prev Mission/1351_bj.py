import sys
sys.setrecursionlimit(100)

N, P, Q = map(int, input().split())

memo = {
    0 : 1
}

def A(i):
    if i in memo:
        return memo[i]

    memo[i] = A(i//P) + A(i//Q)
    return memo[i]


print(A(N))