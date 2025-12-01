from collections import deque
L, W = map(int ,input().split())
board = [list(input().rstrip()) for _ in range(L)]

#보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def is_vaild(y,x):
    return 0 <= y < L and 0 <= x < W

def bfs(y_pos,x_pos,distance):
    deq = deque()
    deq.append((y_pos,x_pos, distance))
    chk = [[False]*W for _ in range(L)]
    chk[y_pos][x_pos] = True
    max_d = 0

    while deq:
        y,x,d= deq.popleft()
        max_d = max(max_d, d)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if is_vaild(ny,nx) and not chk[ny][nx] and board[ny][nx] == "L":
                chk[ny][nx] = True
                deq.append((ny,nx, d+1))
    return max_d

ans = 0

for i in range(L):
    for j in range(W):
        if board[i][j] == "L":
            ans = max(ans, bfs(i,j,0))
print(ans)
