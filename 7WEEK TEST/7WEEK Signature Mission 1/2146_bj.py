from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

# 1. 섬 라벨링
def label_islands():
    label = 2  # 기존 board의 1과 구분하기 위해 2부터 시작
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bfs_label(i, j, label)
                label += 1
    return label

def bfs_label(y, x, label):
    q = deque()
    q.append((y, x))
    board[y][x] = label
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if is_valid(ny, nx) and board[ny][nx] == 1:
                board[ny][nx] = label
                q.append((ny, nx))

# 2. 각 섬에서 바다로 퍼져 다른 섬과의 거리 탐색
def bfs_bridge(start_label):
    visited = [[False] * N for _ in range(N)]
    q = deque()

    # 시작 섬의 모든 칸을 큐에 넣기
    for i in range(N):
        for j in range(N):
            if board[i][j] == start_label:
                q.append((i, j, 0))
                visited[i][j] = True

    while q:
        y, x, d = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_valid(ny, nx) or visited[ny][nx]:
                continue

            # 다른 섬 도착!
            if board[ny][nx] != 0 and board[ny][nx] != start_label:
                return d

            # 바다인 경우 계속 확장
            if board[ny][nx] == 0:
                visited[ny][nx] = True
                q.append((ny, nx, d + 1))

    return 10**9

# 실행 부분
next_label = label_islands()

ans = 10**9

# 각 섬마다 BFS 실행
for label in range(2, next_label):
    ans = min(ans, bfs_bridge(label))

print(ans)
