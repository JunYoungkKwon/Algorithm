import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

def bfs():
    q = deque()
    q.append((0,0))
    check = [False] * n
    check[0] = True

    while q:
        now, depth = q.popleft()

        if depth < 2:

            for nxt in adj[now]:
                if check[nxt] == False:
                    check[nxt] = True
                    q.append((nxt, depth+1))
    return check.count(True)

print(bfs()-1)
