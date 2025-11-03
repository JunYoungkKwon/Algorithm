# 오른쪽 위가 (0,0)
# 왼쪽 아래가 (N-1.M-1)
#
# 0인 경우 북쪽
# 1인 경우 동쪽
# 2인 경우 남쪽
# 3인 경우 서쪽

N, M = map(int, input().split())
y, x, d = map(int, input().split())


board = [list(map(int, input().split()))[::-1] for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def is_vaild(y, x):
    return 0 <= y < N and 0 <= x < M


ans = 0
while True:
    dirty = False

    if board[y][x] == 0:
        board[y][x] = 2
        ans += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_vaild(ny, nx):
            if board[ny][nx] == 0:
                dirty = True

    #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    if dirty:
        #반시계 방향으로 90도 회전
        if d == 0:
            d = 3
        else:
            d = d - 1
        #바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        ny = y + dy[d]
        nx = x + dx[d]
        if board[ny][nx] == 0 and is_vaild(ny, nx):
            y = ny
            x = nx
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        d = (d+2) % 4
        ny = y + dy[d]
        nx = x + dx[d]
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        if board[ny][nx] == 1:
            break
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        else:
            y = ny
            x = nx

print(ans)

# 0 1 2 3
# 2 3 0 1











