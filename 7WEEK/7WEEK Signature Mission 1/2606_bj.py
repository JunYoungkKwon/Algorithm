from collections import deque
N = int(input())
K = int(input())
virus = [[] for _ in range(N)]
chk = [False] * N
for i in range(K):
    #0_base
    a, b = map(lambda x:x-1 ,map(int, input().split()))
    virus[a].append(b)
    virus[b].append(a)
def bfs():
    q = deque()
    q.append(0)
    chk[0] = True
    while q:
        now = q.popleft()
        for nxt in virus[now]:
            if not chk[nxt]:
                chk[nxt] = True
                q.append(nxt)


bfs()
print(chk.count(True)-1)