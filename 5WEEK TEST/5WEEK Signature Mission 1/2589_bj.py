from collections import deque

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs(y_pos, x_pos, h):
    deq = deque()
    deq.append((y_pos, x_pos, h))
    max_time = 0
    while deq:
        y, x, time = deq.popleft()
        max_time = max(max_time, time)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid(ny, nx) and not is_visited[ny][nx] and board[ny][nx] == 'L':
                is_visited[ny][nx] = True
                deq.append((ny, nx, time+1))
    return max_time

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            is_visited = [[False] * M for _ in range(N)]
            is_visited[i][j] = True
            ans = max(ans, bfs(i, j, 0))

print(ans)