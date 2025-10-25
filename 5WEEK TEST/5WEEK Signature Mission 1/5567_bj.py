# 1 - 2 3
# 2 - 1 3
# 3 - 1 2 4
# 4 - 3 5
# 5 - 4
n = int(input()) #상근이의 동기의 수
m = int(input())#리스트의 길이
chk = [0] * (n+1)
friend = [[]for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

chk[1] = 1
for i in friend[1]:
    chk[i] = 1
    for a in friend[i]:
       chk[a] = 1

print(sum(chk)-1)


