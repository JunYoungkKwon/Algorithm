from collections import deque
import sys
input = sys.stdin.readline

def is_valid_coord(x, y):
    return 0 <= y < N and 0 <= x < N

def bfs(fx ,fy, cnt):
    chk[fx][fy] = True
    q = deque()
    q.append((fx, fy, cnt))
    while q:
        x, y, cnt = q.popleft()

        if x == mx and y == my:
            return print(cnt)

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_valid_coord(nx, ny) and not chk[nx][ny]:
                chk[nx][ny] = True
                q.append((nx, ny, cnt + 1))


dy = (2, -2, 2, -2, 1, -1, 1, -1)
dx = (1, 1, -1, -1, 2, 2, -2, -2)

cnt = 0
for _ in range(int(input())):
    N = int(input())
    x, y = map(int, input().split())
    mx, my = map(int, input().split())
    adj = [[0] * N for _ in range(N)]
    chk = [[False] * N for _ in range(N)]
    bfs(x, y, cnt)