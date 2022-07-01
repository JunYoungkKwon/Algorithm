import sys
input =sys.stdin.readline

N, M = map(int, input().split())

s1 =[input().rstrip() for _ in range(N)]
s2 =[input().rstrip() for _ in range(M)]

ans = 0

for i in s2:
    for j in s1:
        if j.startswith(i):
            ans += 1
            break
print(ans)