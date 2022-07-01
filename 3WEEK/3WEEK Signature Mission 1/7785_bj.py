import sys
input = sys.stdin.readline
arr = []
N = int(input())
for _ in range(N):
    A, B = map(str, input().split())
    if B == 'enter':
        arr.append(A)
    else:
        del arr[arr.index(A)]
arr.sort(reverse=True)

for ar in arr:
    print(ar)

