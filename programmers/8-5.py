from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 최대 50 → 2배하면 100
    board = [[0] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]

    # 🔹 모든 좌표 2배 확장
    rectangle = [[x1 * 2, y1 * 2, x2 * 2, y2 * 2] for x1, y1, x2, y2 in rectangle]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    # 사각형 채우기
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                board[y][x] = 1

    # 내부 제거 (테두리만 남김)
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1 + 1, y2):
            for x in range(x1 + 1, x2):
                board[y][x] = 0

    def bfs(start_y, start_x, distance):
        deq = deque()
        deq.append((start_y, start_x, distance))
        visited[start_y][start_x] = True
        while deq:
            y, x, d = deq.popleft()
            if y == itemY and x == itemX:
                return d // 2
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < 102 and 0 <= nx < 102:
                    if board[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        deq.append((ny, nx, d + 1))

    return bfs(characterY, characterX, 0)