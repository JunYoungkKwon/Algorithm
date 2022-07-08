#최단경로 bfs
# -D 실수하지 말자..ㅠ
from collections import deque

F, S, G, U, D = map(int, input().split())

adj = [i for i in range(1,F+1)]
chk = [False] * F

dy = (U, -D)

ans = 0


def is_valid_coord(y):
    return 0 <= y < F

def bfs():
    q = deque()
    q.append((S-1, ans))
    chk[S-1] = True
    while q:
        y, d = q.popleft()
        for k in range(2):
            ny = y + dy[k]
            if is_valid_coord(ny) and not chk[ny]:
                if adj[ny] != G:
                    chk[ny] = True
                    q.append((ny, d + 1))
                if adj[ny] == G:
                    print(d+1)
                    return

    print("use the stairs")

if S==G:
    print(0)
else:
    bfs()

