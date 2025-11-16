from collections import deque

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

# 방향: 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 초기 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            ry, rx = i, j
        if board[i][j] == 'B':
            by, bx = i, j

# 구슬 굴리기 함수
def roll(y, x, dy, dx):
    cnt = 0
    # 벽 만나기 전까지 굴리기
    while True:
        ny = y + dy
        nx = x + dx

        if board[ny][nx] == '#':
            break
        y, x = ny, nx
        cnt += 1
        if board[y][x] == 'O':
            break
    return y, x, cnt


def bfs():
    deq = deque()
    deq.append((ry, rx, by, bx, 0))
    visited = set()
    visited.add((ry, rx, by, bx))

    while deq:
        r_y, r_x, b_y, b_x, depth = deq.popleft()

        if depth >= 10:
            return -1

        for i in range(4):
            nry, nrx, rcnt = roll(r_y, r_x, dy[i], dx[i])
            nby, nbx, bcnt = roll(b_y, b_x, dy[i], dx[i])

            # 파란 구슬이 빠지면 실패
            if board[nby][nbx] == 'O':
                continue

            # 빨간 구슬만 빠지면 성공
            if board[nry][nrx] == 'O':
                return depth + 1

            # 둘이 겹치면 조정 필요
            if nry == nby and nrx == nbx:
                # 더 많이 굴러온 쪽을 한 칸 뒤로
                if rcnt > bcnt:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]

            # 방문 체크
            state = (nry, nrx, nby, nbx)
            if state not in visited:
                visited.add(state)
                deq.append((nry, nrx, nby, nbx, depth + 1))

    return -1


print(bfs())
