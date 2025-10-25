from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

dy =[-1, 1, 0, 0]
dx =[0, 0, -1, 1]

def bfs():
    deq = deque()
    deq.append((0, 0))

    while deq:
        y, x = deq.popleft()
        if y == N-1 and x == M-1:
            return board[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= N-1 and 0 <= nx <= M-1 and board[ny][nx] == 1:
                deq.append((ny, nx))
                board[ny][nx] = board[y][x] + 1

print(bfs())
