from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
max_range = 10**6 +1
visit = [0] * max_range

def is_valid_coord(x):
    return 0 <= x < max_range

def bfs():
    visit[N] = 1
    q =deque()
    q.append((N,0))
    while q:
        x, cnt = q.popleft()
        if x == K:
            print(cnt)
        for nx in [x-1, x+1, x * 2]:
            if is_valid_coord(nx) and not visit[nx]:
                visit[nx] = 1
                q.append((nx, cnt+1))

bfs()



