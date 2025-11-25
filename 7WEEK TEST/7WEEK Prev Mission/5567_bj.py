N = int(input())
m = int(input())

freind = [[] for _ in range(N+1)]
for _ in range(m):
    a, b = map(int, input().split())
    freind[a].append(b)
    freind[b].append(a)

chk = [0] * (N+1)
ans = 0
chk[1] = 1

for i in freind[1]:
    for a in freind[i]:
        if not chk[a]:
            chk[a] = 1
print(sum(chk)-1)




