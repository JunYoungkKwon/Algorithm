from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 아기 상어 초기 위치
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            y, x = i, j
            board[i][j] = 0   # 상어가 있던 자리를 빈 칸으로 변경

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

# 상어 위치에서 BFS → (먹을 수 있는 물고기들의 위치, 거리) 리스트 반환
def bfs_find(y, x, size):
    q = deque()
    q.append((y, x, 0))
    visited = [[False]*N for _ in range(N)]
    visited[y][x] = True

    fish = []  # (거리, y, x) 저장

    while q:
        cy, cx, dist = q.popleft()

        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]

            if not is_valid(ny, nx) or visited[ny][nx]:
                continue

            # 지나갈 수 있는 조건: board <= size
            if board[ny][nx] <= size:
                visited[ny][nx] = True
                q.append((ny, nx, dist + 1))

                # 먹을 수 있는 조건: 1 ~ size-1
                if 1 <= board[ny][nx] < size:
                    fish.append((dist + 1, ny, nx))

    return fish


size = 2
eat_fish = 0
ans = 0

while True:

    # 현재 상어 위치에서 BFS로 먹을 수 있는 물고기 탐색
    fishes = bfs_find(y, x, size)

    # 먹을 수 있는 물고기 없음
    if not fishes:
        print(ans)
        break

    # 거리 → 위 → 왼쪽 순 정렬
    fishes.sort()
    dist, ty, tx = fishes[0]

    # 이동
    ans += dist
    eat_fish += 1
    board[ty][tx] = 0  # 물고기 먹음
    y, x = ty, tx      # 상어 위치 이동

    # 크기 증가
    if eat_fish == size:
        size += 1
        eat_fish = 0
