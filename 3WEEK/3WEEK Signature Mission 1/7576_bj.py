from collections import deque
import sys
#최단 경로 =bfs
#다 1인 경우 = 0, 1이 여러 개, 반복문을 돌고서 0 이 남아 있는 경우
input = sys.stdin.readline
M, N = map(int, input().split())
ans = 0
d = 0
is_tf = True

adj = [list(map(int, input().split())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]

q= deque()

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    global ans
    while q:
        y, x, d = q.popleft()
        ans = max(ans, d)
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx] and adj[ny][nx] == 0:
                chk[ny][nx] = True
                q.append((ny, nx, d+1))

for i in range(N):
    for j in range(M):
        if is_valid_coord(i, j) and adj[i][j] == 1 and not chk[i][j]:
            chk[i][j] = True
            q.append((i, j, d))

bfs()

for i in range(N):
    for j in range(M):
      if adj[i][j] == 0 and chk[i][j] == False:
          is_tf = False
if is_tf:
    print(ans)
else:
    print(-1)