N = int(input()) #보드크기
board = [list(map(int, input().split())) for _ in range(N)]
#보드는 무조건 5번 다 옮기는게 최대값
#상하좌우 움직이면서 최대값 찾는것
#일단 경우의 수는 4**5 상하좌우를 5번 랜덤

# d = 0 1 2 3
# 0  좌 상 우 하
def move(d):
    merged = False
    if d == 0:
        for i in range(N):
            for k in range(len(board[i])-1):
                if board[i][k] != 0:
                    if board[i][k] == board[i][k+1]:
                        board[i][k] = 2*board[i][k]

                else:
                    continue





def find_max():
    max_n = 0
    for i in range(N):
        max_n = max(max_n, max(board[i]))
    return max_n


print(find_max())