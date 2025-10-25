import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    s1 = set()
    for _ in range(N):
        s1.add(int(input()))
    s2 = set()
    for _ in range(M):
        s2.add(int(input()))
    s3 = s1.intersection(s2)
    print(len(s3))

