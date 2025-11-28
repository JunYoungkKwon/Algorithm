from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


ans = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_vaild(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(y_pos, x_pos, d):
    global depth
    deq = deque()
    deq.append((y_pos, x_pos, d))
    chk = [[False] * N for _ in range(N)]
    chk[y_pos][x_pos] = True

    while deq:
        y, x, depth = deq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if is_vaild(ny, nx) and not chk[ny][nx]:
                if board[y][x] < board[ny][nx]:
                    chk[ny][nx] = True
                    deq.append((ny, nx, depth+1))
    return depth

for i in range(N):
    for j in range(N):
        ans = max(ans, bfs(i, j, 1))

print(ans)


#대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다
#판다가 이동할 수 있는 칸의 수의 최댓값을 출력