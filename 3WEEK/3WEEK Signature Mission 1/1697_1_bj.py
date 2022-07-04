from collections import deque
import sys
input = sys.stdin.readline

def is_valid_coord(x):
    return 0 <= x < max_range

def bfs(x, res):
    q = deque()
    q.append(x)
    while q:
        cur = q.popleft()
        if cur == res:
            print(chk[cur])
            break

        for nx in (cur - 1, cur + 1, cur * 2):
            if is_valid_coord(nx) and not chk[nx]:
                chk[nx] = chk[cur] + 1
                q.append(nx)

max_range = 10**5+1
N ,K = map(int, input().split())
chk = [0] * max_range
bfs(N, K)

