#머리와 몸통을 큐로 이용해서 나타내고 다음에 갈 위치가 큐에 있는 좌표면 충돌하는 것임
# 사실 이렇게 머리와 몸통을 어떻게 구분해야 될지 몰라서 참고했음.. 항상 풀던 큐지만 발상의 전환을 하는게 중요한 듯..
from collections import deque
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

L = int(input())
direction = [list(map(str, input().split())) for _ in range(L)]
# 동남서북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N
def is_crashed(ny, nx, q):
    for position in q:
        if position[0] == ny and position[1] == nx:
            return True
    return False

def dummy(y, x, d):
    q = deque()
    q.append((y, x, d))
    time = 0

    while q:
        y, x, d = q[-1]
        # 뱀의 이동 방향 체크
        for i in direction:
            if time == int(i[0]):
                if i[1] == 'D':  #오른쪽
                    d = (d + 1) % 4
                else:  #왼쪽
                    d = (d + 3) % 4
        ny = y + dy[d]
        nx = x + dx[d]
        # 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
        if not is_valid(ny, nx) or is_crashed(ny, nx, q):
            print(time+1)
            break
        # 1.먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
        # 2.만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if board[ny][nx] == 1:
            board[ny][nx] = 0
            q.append((ny, nx, d))

        # 3.만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        else:
            q.append((ny, nx, d))
            q.popleft()

        time += 1


dummy(0, 0, 0)