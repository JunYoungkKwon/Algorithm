import sys
n = int(input())
for _ in range(n):
    x, y = sys.stdin.readline().rstrip().split()
    print(int(x)+int(y))
