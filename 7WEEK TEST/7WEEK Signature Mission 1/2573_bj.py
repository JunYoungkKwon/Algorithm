from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

dq = deque()

def is_vaild(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs_island(i,j,chk):
    deq = deque()
    deq.append((i, j))
    chk[i][j] = True

    while deq:
        y,x = deq.popleft()
        for i in range(4):
            ny,nx = y + dy[i], x + dx[i]

            #이어져있는 빙하 찾기
            if is_vaild(ny, nx) and board[ny][nx] != 0 and not chk[ny][nx]:
                chk[ny][nx] = True
                deq.append((ny, nx))

def cnt_island():
    chk = [[False] * M for _ in range(N)]
    island = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not chk[i][j]:
                bfs_island(i,j, chk)
                island += 1
    return island

def melt():
    melt_board = [[0] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if board[y][x] > 0:
                cnt = 0
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if is_vaild(ny, nx) and board[ny][nx] == 0:
                        cnt += 1
                melt_board[y][x] = cnt

    # 한꺼번에 녹이기
    for y in range(N):
        for x in range(M):
            board[y][x] = max(0, board[y][x] - melt_board[y][x])
year = 0
while True:
    islands = cnt_island()

    #빙산이 2개 이상 되면
    if islands >= 2:
        print(year)
        break

    #빙산이 다 녹으면
    if islands == 0:
        print(0)
        break

    melt()
    year += 1