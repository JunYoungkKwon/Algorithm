# 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
#
#
# 경사로를 놓은 곳에 또 경사로를 놓는 경우
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 경사로를 놓다가 범위를 벗어나는 경우

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chk = [[0]*N for _ in range(N)]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

ans = 0
for i in range(N):
    same = 0
    pre_num = 0
    for j in range(N):
        now_num = board[i][j]
        if abs(pre_num-now_num) == 1:
            if pre_num < now_num :

            if pre_num > now_num:


