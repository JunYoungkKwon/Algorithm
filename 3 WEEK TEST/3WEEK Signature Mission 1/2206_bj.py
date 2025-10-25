from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs(y, x, distance, destroy):
    deq = deque()
    deq.append((y, x, distance, destroy))
    visited[y][x][0] = True

    while deq:
        y, x, distance, destroy = deq.popleft()

        if y == N-1 and x == M-1:
            return  distance

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid_coord(ny, nx) and not visited[ny][nx][destroy]:
                if destroy == 0:
                    if board[ny][nx] == "1":
                        visited[ny][nx][1] = True
                        deq.append((ny, nx, distance+1, 1))
                    else:
                        visited[ny][nx][destroy] = True
                        deq.append((ny, nx, distance + 1, 0))
                else:
                    if board[ny][nx] == "0":
                        visited[ny][nx][destroy] = True
                        deq.append((ny, nx, distance + 1, 1))
                #파괴 한개 했는데 주변이 다 1이면 -1출력 해야함
    return -1

print(bfs(0, 0, 1, 0))
