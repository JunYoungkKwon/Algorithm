N, east, west, north, south = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

prob_li = [east /100, west/100, north/100, south/100]
visited = [[False] * 30 for _ in range(30)]
started_x, started_y = 15, 15
visited[started_y][started_x] = True

answer = 0

def dfs(y, x, depth, prob):
    global answer
    if N == depth:
        answer += prob
        return

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not visited[nx][ny] and prob_li[dir] > 0:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, prob * prob_li[dir])
            visited[nx][ny] = False  # 되돌리기

dfs(started_y, started_x, 0, 1.0)
print(answer)