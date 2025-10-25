from collections import deque
M, N, K = map(int , input().split())

visited = [[False]*N for _ in range(M)]
board = [[0]*N for _ in range(M)]

dy = [0,-1,0,1]
dx = [1,0,-1,0]
ans = []

for i in range(K):
    y, x, ny, nx = map(int , input().split())

    for ky in range(x, nx):
        for kx in range(y, ny):
            board[ky][kx] = 1

def is_valid_coord(y, x):
    return 0 <= y < M and 0 <= x < N

def bfs(y, x):
    deq = deque()
    deq.append((y, x))
    visited[y][x] = 1
    cnt = 1
    while deq:
        ay, ax = deq.popleft()

        for k in range(4):
            ny = ay + dy[k]
            nx = ax + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                deq.append((ny, nx))
                cnt += 1

    ans.append(cnt)

for y in range(M):
    for x in range(N):
        if not visited[y][x] and board[y][x] == 0:
            bfs(y, x)

ans.sort()
print(len(ans))
print(*ans)
