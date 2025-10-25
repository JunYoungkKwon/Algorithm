import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

N, M = map(int, input().split())

adj = [[0] * N for _ in range(N)]

for _ in range(M):
    #제로 베이스를 만들기 위해 람다 사용
    u, v = map(lambda x: x - 1, map(int, input().split()))
    #무방향 = 양방향
    adj[u][v] = adj[v][u] = 1

chk = [False] * N
ans = 0

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        print(i)
        chk[i] = True
        dfs(i)

print(ans)



        










