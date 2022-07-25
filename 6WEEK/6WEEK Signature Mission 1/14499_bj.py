N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
# for i in range(N):
#     print(*board[i])
# 제자리,동,서,북,남
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
dice = [0] * 6
def do_dice(d):
    global dice
    if d == 1:
        dice = [dice[3]] + [dice[1]] + [dice[0]] + [dice[5]] + [dice[4]] + [dice[2]]
    elif d == 2:
        dice = [dice[2]] + [dice[1]] + [dice[5]] + [dice[0]] + [dice[4]] + [dice[3]]
    elif d == 3:
        dice = [dice[4]] + [dice[0]] + [dice[2]] + [dice[3]] + [dice[5]] + [dice[1]]
    else:
        dice = [dice[1]] + [dice[5]] + [dice[2]] + [dice[3]] + [dice[0]] + [dice[4]]


for i in range(K):
    ny = y + dy[order[i]]
    nx = x + dx[order[i]]
    if (ny < 0 or ny >= N) or (nx < 0 or nx >= M):
        continue
    # print(f'order = {order[i]}, ny = {ny} dx = {nx}')
    do_dice(order[i])
    print(dice[0])
    if board[ny][nx] == 0:
        board[ny][nx] = dice[5]

    else:
        dice[5] = board[ny][nx]
        board[ny][nx] = 0
    y = ny
    x = nx