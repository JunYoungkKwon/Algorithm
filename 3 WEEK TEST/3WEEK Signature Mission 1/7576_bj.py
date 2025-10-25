import sys
from collections import deque

# M은 상자의 가로 칸의 수, N은 상자의 세로 칸
# 2 ≤ M, N ≤ 1, 000
# 정수 1은 익은 토마토
# 정수 0은 익지 않은 토마토
# 정수 -1 은 빈칸

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_vaild(y, x):
    return 0 <= y < M and 0<= x < N

def bfs():
    day = 0
    while deq:
        y, x, day = deq.popleft()
        for i in range(4):
            ny = y +dy[i]
            nx = x +dx[i]
            if is_vaild(ny, nx) and not visitd[ny][nx] and not board[ny][nx]:
                visitd[ny][nx] = True
                board[ny][nx] = 1
                deq.append((ny, nx, day+1))
    return day




input = sys.stdin.readline
deq = deque()
N, M = map(int ,input().split())
board = [list(map(int ,input().split())) for _ in range(M)]
visitd = [[False]*N for _ in range(M)]

zero_cnt = sum(row.count(0) for row in board)

for i in range(M):
    for j in range(N):
        if board[i][j] == 1:
            visitd[i][j] = True
            deq.append((i, j, 0))

# BFS 실행
ans = bfs()

# 모든 칸 확인 (안 익은 토마토가 남았는지)
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            print(-1)
            sys.exit()

print(ans)