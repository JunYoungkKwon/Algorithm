#이해했고 구현만 하면 되는데 구현 거의 다 했는데 뭔가 막혀서 참고했음.. ㅠㅠ
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

board = [[0]*101 for _ in range(101)]

N = int(input())
total_dc = set()
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dc = [(y, x)]
    d_list = [d]
    nx = x + dx[d]
    ny = y + dy[d]
    dc.append((ny, nx))
    x = nx
    y = ny
    for i in range(g):
        tmp_d_list = []
        for j in range(len(d_list)-1, -1, -1):
            nx = x + dx[(d_list[j]+1) % 4]
            ny = y + dy[(d_list[j]+1) % 4]
            dc.append((ny, nx))
            x = nx
            y = ny
            tmp_d_list.append((d_list[j]+1) % 4)
        d_list = d_list+tmp_d_list

    for i in dc:
        total_dc.add(i)


for i in total_dc:
    board[i[0]][i[1]] = 1

ans = 0
for i in range(101):
    for j in range(101):
        if i < 100 and j < 100:
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
                ans += 1
print(ans)