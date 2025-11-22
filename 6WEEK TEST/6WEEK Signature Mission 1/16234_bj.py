# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.

from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def is_valid(y,x):
    return 0 <= y < N and 0 <= x < N

def bfs(y, x):
    deq =deque()
    deq.append((y, x))

    chk[y][x] = True

    people = [(y, x)]
    total = board[y][x]


    while deq:
        ypos, xpos = deq.popleft()
        for i in range(4):
            ny, nx = ypos + dy[i], xpos + dx[i]
            if is_valid(ny, nx) and not chk[ny][nx]:
                if L <= abs(board[ypos][xpos] - board[ny][nx]) <= R:
                    chk[ny][nx] = True
                    deq.append((ny, nx))
                    people.append((ny, nx))
                    total += board[ny][nx]
                    #리스트에 값 넣기
    return people, total

ans = 0

while True:
    chk = [[False] * N for _ in range(N)]
    people_move = False

    for i in range(N):
        for j in range(N):
            if not chk[i][j]:
                group, total_pop = bfs(i, j)
                #인구이동 발생o
                if len(group) > 1:
                    people_move = True
                    new_num = total_pop // len(group)

                    for y, x in group:
                        board[y][x] = new_num

    #인구이동 발생x
    if not people_move:
        print(ans)
        break

    ans += 1



