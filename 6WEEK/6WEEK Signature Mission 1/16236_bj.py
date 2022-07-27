from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            sx, sy = i, j
            break
size = 2
move_num = 0
eat = 0
while True:
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        x, y, count = q.popleft()

        if count > flag:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] > size or visited[nx][ny]:
                continue

            if arr[nx][ny] != 0 and arr[nx][ny] < size:
                fish.append((nx, ny, count + 1))
                flag = count
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        eat += 1
        arr[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        sx, sy = x, y
    else:
        break

print(move_num)
# from collections import deque
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
#
# #상좌하우
# dy = [-1, 0, 1, 0]
# dx = [0, -1, 0, 1]
#
# def is_valid(y, x):
#     return 0 <= y < N and 0 <= x < N
#
# #못 먹는 피쉬가 생길 수 있어서 이런 식으로 찾으면 안될 듯
# def no_fish():
#     for i in range(N):
#         for j in range(N):
#             if 1 <= board[i][j] <= 6:
#                 return False
#     return True
# def find_fish(s):
#     fish = 0
#     for i in range(N):
#         for j in range(N):
#             if  board[i][j] < s:
#                 fish += 1
#     return fish
# #아기 상어 size = 2
#
# def bfs(y, x, s, t, exp):
#     q = deque()
#     q.append((y, x, s, t, exp))
#     while q:
#         y, x, s, t, exp = q.popleft()
#
#         if no_fish():
#             return t
#         #자신의 사이즈 수와 갖은 크기의 물고기를 잡으면 사이즈 업
#         if exp == s:
#             s += 1
#
#         for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#             if is_valid(ny, nx):
#                 #고기는 못 먹고 이동만 가능한 경우
#                 if board[ny][nx] == 0 or board[ny][nx] == s:
#                     q.append((ny, nx, s, t+1, exp))
#                 #아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다
#                 # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
#                 if board[ny][nx] < s:
#                     #먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
#                     if find_fish(s) == 1:
#                         pass
#                     #먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
#                     #거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
#                     #거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
#                     if find_fish(s) > 1:
#                         pass
# # 0: 빈 칸 / 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기 / 9: 아기 상어의 위치
# for i in range(N):
#     for j in range(N):
#         if board[i][j] == 9:
#             y, x = i, j
#             break
#
# print(bfs(y, x, 2, 0, 0))