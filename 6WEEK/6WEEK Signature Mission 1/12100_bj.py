import copy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]

def move(k):
    #상
    if k == 0:
        for i in range(N):
            num = []
            cnt = 0
            for j in range(N):
                if board[j][i] != 0:
                    num.append(board[j][i])
            if len(num) == 1:
                board[j][0] == num[-1]
            if len(num) > 1:
                for k in range(len(num) - 1):
                    if num[k] == num[k + 1]:
                        num[k] = (num[k] + num[k + 1])
                        num[k + 1] = 0

                for m in range(len(num)):
                    if num[m] == 0:
                        continue
                    if num[m] != 0:
                        board[m][i] = num[m]
                        cnt += 1
                for n in range(cnt, N):
                    board[n][i] = 0
    # #하
    if k == 1:
        for i in range(N):
            num = []
            cnt = 0
            for j in range(N-1, -1, -1):
                if board[j][i] != 0:
                    num.append(board[j][i])
            if len(num) == 1:
                board[j][N - 1] == num[-1]
            if len(num) > 1:
                for k in range(len(num) - 1):
                    if num[k] == num[k + 1]:
                        num[k] = (num[k] + num[k + 1])
                        num[k + 1] = 0

                for m in range(len(num)):
                    if num[m] == 0:
                        continue
                    if num[m] != 0:
                        board[(N - 1)-m][i] = num[m]
                        cnt += 1
                for n in range(N - cnt):
                    board[n][i] = 0
    #좌
    if k == 2:
        for i in range(N):
            num = []
            cnt = 0
            for j in range(N):
                if board[i][j] != 0:
                    num.append(board[i][j])
            if len(num) == 1:
                board[i][0] == num[-1]
            if len(num) > 1:
                for k in range(len(num)-1):
                    if num[k] == num[k+1]:
                        num[k] = (num[k] + num[k+1])
                        num[k+1] = 0

                for m in range(len(num)):
                    if num[m] == 0:
                        continue
                    if num[m] != 0:
                        board[i][m] = num[m]
                        cnt += 1
                for n in range(cnt, N):
                    board[i][n] = 0
    #우
    if k == 3:
        for i in range(N):
            num = []
            cnt = 0
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    num.append(board[i][j])
            if len(num) == 1:
                board[i][N-1] == num[-1]
            if len(num) > 1:
                for k in range(len(num)-1):
                    if num[k] == num[k+1]:
                        num[k] = (num[k] + num[k+1])
                        num[k+1] = 0

                for m in range(len(num)):
                    if num[m] == 0:
                        continue
                    if num[m] != 0:
                        board[i][(N-1)-m] = num[m]
                        cnt += 1
                for n in range(N-cnt):
                    board[i][n] = 0
def find_max_value():
  value = 0
  for i in range(N):
    for j in range(N):
      value = max(value,board[i][j])
  return value

def backtracking(d):
    global board
    global ans
    if d == 5:
        ans = max(ans, find_max_value())
        return
    current_board = copy.deepcopy(board)
    for i in range(4):
        move(i)
        for k in range(N):
            print(*board[k])
        print("")
        backtracking(d + 1)
        board = copy.deepcopy(current_board)  # 보드 초기화 해줌

ans = 0
# backtracking(0)
print(ans)
move(0)
for k in range(N):
    print(*board[k])
print("")

