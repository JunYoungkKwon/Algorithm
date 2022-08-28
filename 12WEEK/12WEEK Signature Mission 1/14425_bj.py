N, M = map(int, input().split())
dic = {}
ans = 0
for _ in range(N):
    dic[input()] = 0
for _ in range(M):
    if input() in dic:
        ans += 1

print(ans)


