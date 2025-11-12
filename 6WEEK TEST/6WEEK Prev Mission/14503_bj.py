# 0인 경우 북쪽,
# 1인 경우 동쪽,
# 2인 경우 남쪽,
# 3인 경우 서쪽

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# c = M-c-1 #c위치를 저장

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def is_valid(y, x):
    return 0 <= y <N and 0 <= x < M

y, x = r, c
cnt = 0
while True:

    empty = False

    #빈칸이면 청소
    if board[y][x] == 0:
        cnt += 1
        board[y][x] = 2

    #한칸씩 돌고 빈 칸이 있으면 실행
    for i in range(4):
        d = (d+3) % 4
        ny = y + dy[d]
        nx = x + dx[d]
        if is_valid(ny, nx):
            if board[ny][nx] == 0:
                y = ny
                x = nx
                empty = True
                break
    #빈칸이 없다면 실행
    if not empty:
        back = (d + 2) % 4
        ny = y + dy[back]
        nx = x + dx[back]
        if not is_valid(ny, nx) or board[ny][nx] == 1:
            break  # 후진 불가능 → 종료
        y, x = ny, nx  # 벽이 아니면 후진

print(cnt)