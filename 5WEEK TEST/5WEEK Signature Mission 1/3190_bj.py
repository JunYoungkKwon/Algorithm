from collections import deque
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
N = int(input()) #보드크기
K = int(input()) #사과 갯수

apple_pos = [list(map(lambda x: int(x)-1, input().split())) for _ in range(K)]

L = int(input()) #뱀의 방향 변환 횟수

snake_info = [list(input().split()) for _ in range(L)]

board = [[0]*N for _ in range(N)]

#사과 표시
for y, x in apple_pos:
    board[y][x] = 2


def is_vaild(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(a, b, t, l):
    deq = deque()
    deq.append((0, 0, 0, 0))
    board[0][0] = 1

    while snake_info:
        y, x, time, len = deq.popleft()
        nx = x+1 #직진
        ry = y+1 #우회전
        ly = y-1 #좌회전
        #방향 변환 시간
        if int(snake_info[0][0]) == time:
            #방향 전환 사용해서 제거
            snake_info.remove(snake_info[0])
            #우회전
            if snake_info[0][1] == 'D':
                #사과가 있음
                if is_vaild(ry, x) and board[ry][x] == 2:
                    deq.append((ry, x, time+1, len+1))
                    board[ry][x] = 1
                else:
                    return time+1
            #좌회전
            else:
                if is_vaild(ly, x):
                    deq.append((ly, x, time+1, len+1))
                    board[ly][x] = 1
                else:
                    return time+1
        #직진
        else:
            if is_vaild(y, nx):
                deq.append((ly, nx, time + 1, len + 1))
                board[y][nx] = 1
            else:
                return time + 1


