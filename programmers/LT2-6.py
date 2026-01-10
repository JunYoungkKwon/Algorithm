# [벡준] 구슬탈출
from collections import deque
N, M = map(int, input().split())
board = [input() for _ in range(N)]

dy = [1,-1,0,0]
dx = [0,0,-1,1]

def bfs(y_pos, x_pos, color):
    deq_red =deque()
    deq_red.append((y_pos, x_pos, color))
    visited = [[False]*M for _ in range(N)]
    visited[y_pos][x_pos] = True
    while deq_red:
        y, x, col = deq_red.popleft()
        for i in range(4):


    #움직임 동시제어

#R,B 시작위치
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            bfs(i,j, 'R')

        if board[i][j] == "B":
            bfs(i, j, 'B')





