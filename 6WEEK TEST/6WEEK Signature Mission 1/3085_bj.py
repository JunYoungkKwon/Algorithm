# 사탕의 색이 다른 인접한 두 칸을 고른다
# 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y

N = int(input())
board = [list(input().strip()) for _ in range(N)]
#x축에서 바꾸고 y축에서 바꾸고 바꿀 때마다 최대 갯수 체크

def check_max_len():
    x_cnt = 1
    y_cnt = 1
    max_cnt = 1
    for i in range(N):
        x_cnt = 1
        for j in range(N-1):
            #x축 같은지 비교
            if board[i][j] == board[i][j+1]:
                x_cnt += 1
                max_cnt = max(max_cnt, x_cnt)
            else:
                x_cnt = 1
    for j in range(N):  # 열 고정
        y_cnt = 1
        for i in range(1, N):  # 행을 아래로 이동
            if board[i][j] == board[i - 1][j]:
                y_cnt += 1
                max_cnt = max(max_cnt, y_cnt)
            else:
                y_cnt = 1

    return max_cnt

ans = 1


def backtracking(y, x):
    global ans


    for i in range(N):
        for j in range(N-1):
            #x축 바꾸기
            if board[i][j] != board[i][j+1]:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                ans = max(ans, check_max_len())
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

    for i in range(N-1):
        for j in range(N):
            #x축 바꾸기
            if board[i][j] != board[i+1][j]:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                ans = max(ans, check_max_len())
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
backtracking(0, 0)

print(ans)
