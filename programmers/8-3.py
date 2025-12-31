from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(maps):
    len_y = len(maps)
    len_x = len(maps[0])

    visited = [[False] * len_x for _ in range(len_y)]

    def bfs():
        deq = deque()
        deq.append((0, 0, 1))
        visited[0][0] = True
        while deq:
            y, x, d = deq.popleft()
            if y == len_y - 1 and x == len_x - 1:
                return d
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < len_y and 0 <= nx < len_x:
                    if not visited[ny][nx] and maps[ny][nx] == 1:
                        visited[ny][nx] = True
                        deq.append((ny, nx, d + 1))
        return -1

    return bfs()
