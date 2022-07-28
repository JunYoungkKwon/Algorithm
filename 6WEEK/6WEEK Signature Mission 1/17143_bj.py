R, C, M = map(int, input().split())
board = [[0]* C for _ in range(R)]
ans = 0
shark_list = []
new_shark_list = []
#상하좌우
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

def get_next_loc(i, j, speed, dir):
    if dir == 1 or dir == 2:  # i
        cycle = R * 2 - 2
        if dir == 1:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= R:
            return (2 * R - 2 - speed, j, 1)
        return (speed, j, 2)

    else:  # j
        cycle = C * 2 - 2
        if dir == 4:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, 2 * C - 2 - speed, 4)
        return (i, speed, 3)

def shark_remove(y, x):
    for shark in shark_list:
        if shark[0] == y and shark[1] == x:
            shark_list.remove(shark)
def new_shark_remove(y, x):
    for shark in new_shark_list:
        if shark[0] == y and shark[1] == x:
            new_shark_list.remove(shark)

def shark_move():
    global board, shark_list, new_shark_list  # board[i][j] 안에는 (s,d,z)의 값이 들어있음. 상어가 없는 경우엔 0이 들어있음
    new_board = [[0]* C for _ in range(R)]
    #기존 보드에 있던 샤크는 지우고 이동한 샤크를 보드에 넣어줘야 함
    # 이동할 수 있는 지도 체크 해야 함
    # 그리고 이동 했는데 거기에 값이 있는 경우도 고려해야 함
    #(r,c)/s = 속력/d = 이동방향/ z = 크기
    # r,c,s,d,z
    # i, j, speed, dir
    # s,d,z
    new_shark_list = []

    for shark in shark_list:
        #board[shark[0]][shark[1]] = 0 이렇게 하면 삭제되지 않은 거랑 기존에 것이랑 충돌 할 수 있음 그래서 한번에 다 초기화

        ny, nx, nd = get_next_loc(shark[0], shark[1], shark[2], shark[3])
        if new_board[ny][nx]:
            #새로운 게 더 크다면 새로운 값으로 넣어줌 아니라면 그냥 그대로
            if new_board[ny][nx][2] < shark[4]:
                new_board[ny][nx] = (shark[2], nd, shark[4])
                #기존 샤크는 지운다
                new_shark_remove(ny, nx)
                new_shark_list.append((ny, nx, shark[2], nd, shark[4]))

        else:
            new_board[ny][nx] = (shark[2], nd, shark[4])
            new_shark_list.append((ny, nx, shark[2], nd, shark[4]))
    # print(shark_list)
    # print("")
    # print(new_shark_list)
    shark_list = new_shark_list
    #샤크리스트 갱신 해야 됨
    # for i in range(R):
    #     print(*new_board[i])
    # print("")
    board = new_board



for _ in range(M):
    #(r,c)/s = 속력/d = 이동방향/ z = 크기
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = (s, d, z)
    shark_list.append((r-1, c-1, s, d, z))

#1.낚시왕이 오른쪽으로 한 칸 이동한다.
for i in range(C):
    shark = []
    for j in range(R):
        if board[j][i]:
            shark.append((j, i, board[j][i][0], board[j][i][1], board[j][i][2]))
    #2-1.낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
    if len(shark) >= 1:
        ans += shark[0][4]
        #2-2.상어를 잡으면 격자판에서 잡은 상어가 사라진다.
        board[shark[0][0]][shark[0][1]] = 0
        shark_remove(shark[0][0], shark[0][1])
    #샤크가 없으면 이동이 불가능 하니 탈출
    # 3.상어가 이동한다.
    # for i in range(R):
    #     print(*board[i])
    # print(ans)
    shark_move()
    # for i in range(R):
    #     print(*board[i])
    # print(ans)
print(ans)
# for i in range(R):
#     print(*board[i])
# print(board[1][3])



