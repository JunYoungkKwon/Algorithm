# CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향
# 지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호 감시할 수 있는 영역을 '#'
# 사각 지대의 최소 크기를 구하기
#
# 1번 0,1,2,3
# 2번 0,2 / 1,3
# 3번 0,1 / 1.2 / 2,3 / 3,0
# 4번 0,1,3 / 0,1,2 / 1,2,3 /2,3,0
# 5번 0123

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]
cctv_list = []
ans = 65

#cctv 위치 파악
for i in range(N):
    for j in range(M):
        if  1 <= board[i][j] <= 5:
            cctv_list.append((i,j,board[i][j]))

def chk_zero():
    cnt = sum(row.count(0) for row in board)
    return cnt

def cctv(num, y, x):

    if num == 1:
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:



def backtracking(depth):
    global ans
    #표시 다 했으면 사각지대 파악
    if depth == len(cctv_list):
        ans = min(ans, chk_zero())

    for cctv_pos in cctv_list:
        y,x,num = cctv_pos
        cctv(num, y, x)
        backtracking(depth+1)



backtracking(0)






