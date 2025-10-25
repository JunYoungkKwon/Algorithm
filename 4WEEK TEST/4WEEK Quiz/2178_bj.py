from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = [list((input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def is_valid(y,x):
    return 0<= y <N and 0<= x < M

def bfs():
    deq = deque()
    deq.append((0,0,1))
    visited[0][0] = True
    while deq:
        y, x, time = deq.popleft()

        if y == N-1 and x == M-1:
            return time

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid(ny, nx) and not visited[ny][nx]:
                if board[ny][nx] == '1':
                    visited[ny][nx] = True
                    deq.append((ny, nx, time+1))




print(bfs())



