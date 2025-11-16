
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
# 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시
#
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다
#
# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값 출력

import sys
input = sys.stdin.readline

N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위 (인덱스 1~6 사용)
dice = [0]*7

# 동, 서, 북, 남
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

def roll(dir):
    top, bottom = 1, 6
    east, west = 3, 4
    north, south = 2, 5

    if dir == 1:   # 동
        dice[top], dice[west], dice[bottom], dice[east] = \
        dice[west], dice[bottom], dice[east], dice[top]

    elif dir == 2: # 서
        dice[top], dice[east], dice[bottom], dice[west] = \
        dice[east], dice[bottom], dice[west], dice[top]

    elif dir == 3: # 북
        dice[top], dice[south], dice[bottom], dice[north] = \
        dice[south], dice[bottom], dice[north], dice[top]

    elif dir == 4: # 남
        dice[top], dice[north], dice[bottom], dice[south] = \
        dice[north], dice[bottom], dice[south], dice[top]


for d in commands:
    ny = y + dy[d]
    nx = x + dx[d]

    # 범위 벗어나면 무시
    if not (0 <= ny < N and 0 <= nx < M):
        continue

    # 위치 갱신
    y, x = ny, nx
    roll(d)

    # 지도와 값 상호작용
    if board[y][x] == 0:
        board[y][x] = dice[6]
    else:
        dice[6] = board[y][x]
        board[y][x] = 0

    # 윗면 출력
    print(dice[1])
