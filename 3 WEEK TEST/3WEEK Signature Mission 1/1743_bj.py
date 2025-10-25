from collections import deque

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
game = [[] for _ in range(N+1)]
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    deq =deque()
    deq.append((y, x))
    board[y][x] = 0
    ans = 1
    while deq:
        ay, ax = deq.popleft()
        for i in range(4):
            ny = ay + dy[i]
            nx = ax + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1:
                board[ny][nx] = 0
                deq.append((ny, nx))
                ans += 1
    return ans

max_size = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            max_size = max(max_size, bfs(i, j))

print(max_size)


