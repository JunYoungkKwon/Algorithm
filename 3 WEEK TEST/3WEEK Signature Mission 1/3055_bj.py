from collections import deque

# 비어있는 곳은 '.'
# 물이 차있는 지역은 '*'
# 돌은 'X'
# 비버의 굴은 'D'
# 고슴도치의 위치는 'S'
# 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

water = deque()
hedgehog = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':  # 고슴도치 시작점
            hedgehog.append((i, j, 0))  # (y, x, 이동시간)
            visited[i][j] = True
        elif board[i][j] == '*':  # 물의 시작점
            water.append((i, j))

def is_valid(y, x):
    return 0 <= y < R and 0 <= x < C

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while hedgehog:
        # 1️⃣ 먼저 물이 확장됨
        for _ in range(len(water)):
            y, x = water.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if is_valid(ny, nx) and board[ny][nx] == '.':
                    board[ny][nx] = '*'
                    water.append((ny, nx))

        # 2️⃣ 그 다음 고슴도치 이동
        for _ in range(len(hedgehog)):
            y, x, time = hedgehog.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if not is_valid(ny, nx) or visited[ny][nx]:
                    continue
                if board[ny][nx] == 'D':
                    return time + 1
                if board[ny][nx] == '.':
                    visited[ny][nx] = True
                    hedgehog.append((ny, nx, time + 1))
    return "KAKTUS"

print(bfs())









