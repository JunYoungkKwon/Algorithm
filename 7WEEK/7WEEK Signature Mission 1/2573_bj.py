from collections import deque
N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
ice = []
new_ice = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if iceberg[i][j] != 0:
            ice.append((i, j))

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs(y, x):
    global new_ice
    q = deque()
    q.append((y, x))
    chk[y][x] = 1
    board = []
    new_ice = []
    while q:
        y, x = q.popleft()
        zero_cnt = 0
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid(ny, nx) and iceberg[ny][nx] == 0:
                zero_cnt +=1
            if is_valid(ny, nx) and iceberg[ny][nx] != 0 and not chk[ny][nx]:
                q.append((ny, nx))
                chk[ny][nx] = 1

        if iceberg[y][x] <= zero_cnt:
            board.append((y, x, 0))
        else:
            board.append((y, x, iceberg[y][x] - zero_cnt))
            new_ice.append((y, x))
    for b in board:
        if b[2] == 0:
            iceberg[b[0]][b[1]] = 0
        else:
            iceberg[b[0]][b[1]] = b[2]
    return 1
y = 0
while ice:
    chk = [[0] * M for _ in range(N)]
    g = 0
    for i in ice:
        if not chk[i[0]][i[1]]:
            g += bfs(i[0], i[1])
    # print(len(new_ice))
    # for k in range(N):
    #     print(*iceberg[k])
    # print("")
    if g > 1:
        print(y)
        break
    ice = new_ice
    y += 1

if g < 2:
    print(0)