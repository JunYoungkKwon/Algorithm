from collections import deque

dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,-1,-1,1,1]


def is_vaild(y, x):
    return 0 <= y < h and 0 <= x < w

def bfs(y, x):
    deq = deque()
    deq.append((y, x))
    visited[y][x] = 1
    while deq:
        ay, ax = deq.popleft()
        for i in range(8):
            ny = ay + dy[i]
            nx = ax + dx[i]
            if is_vaild(ny, nx) and not visited[ny][nx] and board[ny][nx] == 1:
                deq.append((ny,nx))
                visited[ny][nx] = 1
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)

