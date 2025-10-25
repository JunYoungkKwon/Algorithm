#이동 하는데 돌이 있으면 킹은 돌의 위치로 돌을 킹이 움직인 방향으로 이동
#만약 돌이나 킹이 보드의 범위를 벗어나면 그 움직임은 건너 뜀

king_pos, stone_pos, N= input().split()

board = [[0]*8 for _ in range(8)]
king_x = ord(king_pos[0])-65
king_y = 8-int(king_pos[1])

stone_x = ord(stone_pos[0])-65
stone_y = 8-int(stone_pos[1])

dirs = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

def is_valid(y, x):
    return 0 <= y < 8 and 0<= x < 8

for i in range(int(N)):
    move = input()
    dy, dx = dirs[move]

    ny, nx = king_y + dy, king_x + dx

    #킹이 보드 범위 밖이면 스킵
    if not is_valid(ny, nx):
        continue

    # 킹 이동 위치가 돌 위치면 → 돌도 밀어야 함
    if ny == stone_y and nx == stone_x:
        sy, sx = stone_y + dy, stone_x + dx
        if not is_valid(sy, sx):
            continue  # 돌이 밀려서 밖으로 나가면 스킵
        stone_y, stone_x = sy, sx  # 돌 이동

        # 킹 이동
    king_y, king_x = ny, nx

# 결과 출력 (좌표를 다시 문자로 변환)
print(chr(king_x + 65) + str(8 - king_y))
print(chr(stone_x + 65) + str(8 - stone_y))
