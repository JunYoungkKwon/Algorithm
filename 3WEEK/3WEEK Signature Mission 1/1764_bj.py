import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s1 = set(input().strip() for _ in range(N))
s2 = set(input().strip() for _ in range(M))
s3 = sorted(s1 & s2)
print(len(s3))
for i in s3:
    print(i)
