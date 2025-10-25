#시간초과나서 재귀 형태로는 pypy3로 제출해야됨
#스택형태로 진행하면 괜찮

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
chk = [[False] * C for _ in range(R)]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ans = 0
def backtracking(y, x, alphabet):
    global ans
    ans = max(ans, len(alphabet))
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if board[ny][nx] not in alphabet and not chk[ny][nx]:
                chk[ny][nx] = True
                backtracking(ny, nx, alphabet + board[ny][nx])
                chk[ny][nx] = False

backtracking(0, 0, board[0][0])

print(ans)

# import sys
#
# r, c = map(int, sys.stdin.readline().split())
# graph = []
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# for _ in range(r):
#     graph.append(list(sys.stdin.readline().strip()))
#
# def dfs(sx, sy):
#     q = set()
#     q.add((sx, sx, graph[sx][sy]))
#     squares = 0
#
#     while q:
#         x, y, now_visited = q.pop()
#
#         squares = max(squares, len(now_visited))
#         if squares == 26:
#             return 26
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if (0 <= nx < r) and (0 <= ny < c) and graph[nx][ny] not in now_visited:
#                 q.add((nx, ny, now_visited + graph[nx][ny]))
#
#     return squares
#
# print(dfs(0, 0))