import sys
from collections import deque
input = sys.stdin.readline

# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
# 벽에는 불이 붙지 않는다
# 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다
# 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


T = int(input())

def is_valid(y, x):
    return 0 <= y < h and 0 <= x < w

def bfs():
    while hero:
        for _ in range(len(fire)):
            y, x = fire.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if is_valid(ny, nx) and board[ny][nx] == '.':
                    board[ny][nx] = '*'
                    fire.append((ny, nx))


        for _ in range(len(hero)):
            y, x, count = hero.popleft()
            if y == 0 or y == h-1 or x == 0 or x == w-1:
                return count

            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if is_valid(ny, nx) and not visited[ny][nx] and board[ny][nx] == '.':
                    visited[ny][nx] = True
                    hero.append((ny, nx, count+1))

    return "IMPOSSIBLE"

for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    #큐를 반복할때마다 초기화 시켜줘야 돼서 여기에 넣음
    fire = deque()
    hero = deque()
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            #불의 위치
            if board[i][j] == '*':
                fire.append((i, j))

            #상근의 위치
            elif board[i][j] == '@':
                hero.append((i, j, 1))
                visited[i][j] = True

    print(bfs())