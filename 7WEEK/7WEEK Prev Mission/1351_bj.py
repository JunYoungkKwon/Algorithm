cache = dict()
cache[0] = 1


def A(i):
    if i not in cache:
        cache[i] = A(i // P) + A(i // Q)

    return cache[i]

N, P, Q = map(int, input().split())
