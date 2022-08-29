import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
x = [input().rstrip() for i in range(N)]
y = dict()

for i in range(N):
    y[x[i]] = str(i + 1)

z = dict(map(reversed, y.items()))

for i in range(M):
    a = input().rstrip()
    if a.isdigit():
        print(z[a])
    else:
        print(y[a])