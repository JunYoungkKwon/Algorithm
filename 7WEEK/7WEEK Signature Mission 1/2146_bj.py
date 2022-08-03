from collections import deque
import copy
N = int(input())
board = [list(map(int , input().split())) for _ in range(N)]
chk = [[0] * N for _ in range(N)]
land = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
d = 1
d_ans = 10000
min_ans = 10000

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(y, x, d):
    q = deque()
    q.append((y, x, d))
    chk[y][x] = d
    while q:
        y, x, d = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid(ny, nx) and board[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = d
                q.append((ny, nx, d))
    return 1

#호출 할 때마다 chk 함수 갱신 해야 됨
def find_bfs(y, x, d, ans):
    global d_ans
    new_chk = copy.deepcopy(chk)
    q = deque()
    q.append((y, x, d, ans))
    while q:
        y, x, d, ans = q.popleft()

        if d_ans < ans:
            break

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nans = ans + 1

            #다른 섬이거나 0이라면 실행
            if is_valid(ny, nx) and (new_chk[ny][nx] > d or not new_chk[ny][nx]):

                #다음 좌표가 0값이라면 -1로 구분
                if not new_chk[ny][nx]:
                    new_chk[ny][nx] = -1
                    q.append((ny, nx, d, nans))
                # 출발 섬이랑 다른 섬이라면 -로 구분해서 간 곳으로 체크
                if new_chk[ny][nx] > d:
                    # 출발 섬이랑 다른 섬이지만 현재 좌표의 섬이랑 다음 좌표의 섬이 같으면 갈 필요 X
                    if abs(new_chk[y][x]) == abs(new_chk[ny][nx]):
                        continue
                    # 출발 섬이랑 다른 섬이고 현재 좌표 섬이랑 다음 좌표의 섬이 다르다
                    else:
                        new_chk[ny][nx] = -(new_chk[ny][nx])
                        q.append((ny, nx, d, nans))
                        d_ans = min(d_ans, nans)

    # for k in range(N):
    #     print(*new_chk[k])
    # print("")
    # print(d_ans-1)
    return d_ans-1

#육지 좌표 획득
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            land.append((i, j))
# print(*land)

#각 섬을 다른 숫자로 표현
for la in land:
    if not chk[la[0]][la[1]]:
        d += (bfs(la[0], la[1], d))

# for k in range(N):
#     print(*chk[k])


for i in range(N):
    for j in range(N):
        for land_num in range(1, d+1):
            if chk[i][j] == land_num:
                min_ans = min(min_ans, find_bfs(i, j,land_num, 0))
                break
print(min_ans)
