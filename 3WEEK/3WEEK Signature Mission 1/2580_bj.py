#빈칸을 다 채웠을 때 return을 했는데 그렇게 되면 계속 dfs를 돌면서 값을 출력하기 때문에 for문을 한번 돌고나면 종료 해야 되;ㅁ
board = [list(map(int, input().split())) for _ in range(9)]

# 0이 존재하는 위치를 받아준다.
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

def chkCol(y, num):
    for i in range(9):
        if num == board[y][i]:
            return False
    return True

def chkRow(x, num):
    for i in range(9):
        if num == board[i][x]:
            return False
    return True

def chk_3by3(y, x, num):
    ny = y // 3 * 3
    nx = x // 3 * 3
    for i in range(3):
        for j in range(3):
            if num == board[ny+i][nx+j]:
                return False
    return True



def dfs(idx):

    if idx == len(blank):
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10):
        y = blank[idx][0]
        x = blank[idx][1]

        if chkRow(x, i) and chkCol(y, i) and chk_3by3(y, x, i):
            board[y][x] = i
            dfs(idx + 1)
            board[y][x] = 0

dfs(0)
