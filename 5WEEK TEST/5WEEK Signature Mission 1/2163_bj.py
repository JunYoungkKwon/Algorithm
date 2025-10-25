N, M = map(int , input().split())

ans = 0
if N == 1 and M == 1:
    print(ans)
else:
    print((N*M)-1)