N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
visited =[[False]*N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = []

def is_valid(y,x):
    return 0 <= y < N and 0 <= x < N

def dfs(y, x):
    apart = 1
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_valid(ny, nx) and not visited[ny][nx] and board[ny][nx] == "1":
            apart += dfs(ny, nx)

    return apart

for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j] == "1":
            ans.append(dfs(i, j))

print(len(ans))  # 총 단지 수
for a in sorted(ans):
    print(a)