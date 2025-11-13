# 사과를 먹으면 뱀 길이가 늘어난다
# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

from collections import deque
N = int(input())#보드크기
K = int(input())#사과개수
apple = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())#방향변환횟수
info = [tuple(input().split()) for _ in range(L)]#방향정보
board = [[0]*N for _ in range(N)]

for y,x in apple:
    board[y-1][x-1] = 2


dy = [-1,0,1,0]
dx = [0,1,0,-1]


def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(y, x, t, d):
    deq = deque()
    deq.append((y, x))
    board[y][x] = 1
    time = t
    idx = 0
    while True:
            time += 1
            ny = y + dy[d]
            nx = x + dx[d]
            #방향전환 시간
            if info:
                if info[0][0] == time:
                    if info[0][1] == 'D':
                        d = (d + 1) % 4
                    else:
                        d = (d + 3) % 4
                    del info[0]


            if is_valid(ny, nx):
                #사과 있는 경우
                if board[ny][nx] == 2:
                    board[ny][nx] = 1
                    deq.append((ny, nx))
                #사과 없는 경우
                elif board[ny][nx] == 0:
                    i, j = deq.popleft()
                    board[i][j] = 0
                    deq.append((ny, nx))
                #내 몸과 부딪힌 경우
                else:
                    print(time)
                    return
            #벽에 부딪힘
            else:
                print(time)
                return


bfs(0, 0, 0, 1)



