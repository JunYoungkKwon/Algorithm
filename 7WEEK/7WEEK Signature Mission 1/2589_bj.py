from collections import deque
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs(i, j, d):
    q = deque()
    q.append((i, j, d))
    cnt = 0
    while q:
        y, x, d = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d + 1
            if is_valid(ny, nx) and board[ny][nx] == "L" and not chk[ny][nx]:
                chk[ny][nx] = True
                # print(f'ny ={ny} nx = {nx} nd = {nd}')
                cnt = max(cnt, nd)
                q.append((ny, nx, nd))
            else:
                continue
    return cnt

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "L":
            # print(f'i ={i} j = {j}')
            chk = [[False] * M for _ in range(N)]
            chk[i][j] = True
            ans = max(ans, bfs(i, j, 0))
print(ans)