# 문제에 주어진 순서대로 dy,dx를 정의해줌
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

# 초기 board를 정의해 줌
board = [[0]*101 for _ in range(101)]

# 각 generation별 좌표를 구해줌
# 드래곤 커브의 좌표를 구해줌
N = int(input())
total_dc = set()
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dc = [(y, x)] #dragon curve의 좌표를 받아주는 리스트
    d_list = [d] #d를 받아주는 리스트
    # 0세대 더해줌
    nx = x + dx[d]
    ny = y + dy[d]
    dc.append((ny, nx))
    x = nx
    y = ny
    for i in range(g): #세대만큼 반복을 돌려줌
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

# 드래곤 커브를 표시해줌
for i in total_dc:
    board[i[0]][i[1]] = 1

# 네 꼭지점이 모두 드래곤 커브의 일부인 것의 개수를 구하여 출력해준다.
ans = 0
for i in range(101):
    for j in range(101):
        if i < 100 and j < 100:
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
                ans += 1
print(ans)