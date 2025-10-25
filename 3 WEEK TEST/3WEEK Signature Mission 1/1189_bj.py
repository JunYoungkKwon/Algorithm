# 한수는 똑똑하여 한번 지나친 곳을 다시 방문하지는 않는다
# T로 표시된 부분은 가지 못하는 부분
#
# R(1 ≤ R ≤ 5), C(1 ≤ C ≤ 5), K(1 ≤ K ≤ 25(R*C))

R, C, K = map(int, input().split())
board =  [list(input().rstrip()) for _ in range(R)]
ans = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def backtracking(y, x, distance):
    global ans

    #집에 도착했는데 거리가 K면 정답 추가
    if y == 0 and x == C-1:
        if distance == K:
            ans += 1
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == '.':
            # 다음 위치를 가는 걸 선택한 경우
            board[ny][nx] = 'X'
            backtracking(ny, nx, distance+1)
            # 다음 위치를 가는 걸 미선택한 경우
            board[ny][nx] = '.'

board[R-1][0] = 'X'
backtracking(R-1, 0, 1)
print(ans)

# 시작은 (R-1, 0)
# 종료는 (0, C-1)
