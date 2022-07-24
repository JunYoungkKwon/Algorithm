from collections import deque
N, L, R= map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N
def is_changed(y, x, ny, nx):
    #국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다
    if L <= abs(board[y][x] - board[ny][nx]) <= R:
        return True
    return False

def bfs(y, x, num):
    check[y][x] = 1
    q = deque()
    q.append((y, x, num))
    union = []
    union.append((y, x, num))
    while q:
        y, x, n = q.popleft()
        for k in range(4):
            ny = y +dy[k]
            nx = x + dx[k]
            if is_valid(ny, nx) and is_changed(y, x, ny, nx) and not check[ny][nx]:
                check[ny][nx] = 1
                q.append((ny, nx, board[ny][nx]))
                union.append((ny, nx, board[ny][nx]))
    return union

cnt = 0
while True:
    check = [[0] * N for _ in range(N)]
    is_tf = False
    for j in range(N):
        for i in range(N):
            if check[j][i] == 0:
                union = bfs(j, i, board[j][i])
                if len(union) > 1:
                    is_tf = True
                    sum = 0
                    for uni in union:
                        sum += uni[2]
                    sum = sum // len(union)
                    for uni in union:
                        board[uni[0]][uni[1]] = sum
    if not is_tf:
        break
    cnt += 1
print(cnt)