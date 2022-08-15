floor = []
t = 1
for _ in range(int(input()) * 2):
    if t % 2 == 0:
        floor.append(int(input()) - 1)
    else:
        floor.append(int(input()) + 1)
    t += 1
# print(*floor)
board = [[1] * 17 for _ in range(17)]

for i in range(1, 16):
    for j in range(1, 16):
        board[i][j] = board[i][j-1] + board[i-1][j]

# for i in range(16):
#     print(*board[i])
for k in range(0, len(floor), +2):
    print(board[floor[k]][floor[k+1]])