dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

N, M = map(int, input().split())
y, x, d = map(int, input().split())

# 0: 빈칸, 1: 벽, 2: 청소한 칸
board = [list(map(int, input().split())) for _ in range(N)]


def search_left():
    global y, x, d

    # 2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    # 2-2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    for _ in range(4):
        left_d = (d + 3) % 4
        left_y = y + dy[left_d]
        left_x = x + dx[left_d]
        d = left_d

        if board[left_y][left_x] == 0:
            y = left_y
            x = left_x
            return True

    return False


while True:
    # 1. 현재 위치를 청소한다.
    board[y][x] = 2

    if search_left():
        continue

    back_d = (d + 2) % 4
    back_y = y + dy[back_d]
    back_x = x + dx[back_d]

    # 2-4. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    if board[back_y][back_x] == 1:
        break

    # 2-3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    else:
        y = back_y
        x = back_x

print(sum(row.count(2) for row in board))  # O(N^2)

for row in board:
    print(row)