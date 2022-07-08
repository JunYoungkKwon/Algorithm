#최단 경로 bfs
#사람이 지나간 곳은 불이 지나갈 수 있기 때문에 체크를 안해줬고 -> 메모리 초과
# 사람이 지나가는 곳도 체크를 해줘도 결과에 영향이 없음
from collections import deque
import sys
input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    while q:
        y, x, d, m = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d + 1
            if is_valid_coord(ny, nx) and not chk[ny][nx] and (adj[ny][nx] == "." or adj[ny][nx] == "@"):
                if m == "fire":
                    chk[ny][nx] = True
                    q.append((ny, nx, nd, f))
                if m == "start":
                    chk[ny][nx] = True
                    q.append((ny, nx, nd, s))
            if not is_valid_coord(ny, nx):
                if m == "start":
                    print(nd)
                    return
    return print("IMPOSSIBLE")

d= 0
s = "start"
f = "fire"
for _ in range(int(input())):
    M, N = map(int, input().split())
    adj = [input().strip() for _ in range(N)]
    chk = [[False] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if is_valid_coord(i, j) and not chk[i][j]:
                if adj[i][j] == "@":
                    chk[i][j] = True
                    start = (i, j, d, s)
                if adj[i][j] == "*":
                    chk[i][j] = True
                    q.append((i, j, d, f))
    q.append(start)
    bfs()
