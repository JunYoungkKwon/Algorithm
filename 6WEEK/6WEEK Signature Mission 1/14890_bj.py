#예외처리가 미숙해서 완전 오래걸렸음 ㅠ
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

#행
ans = 0
for i in range(N):
    same = 1
    for j in range(N-1):
        if same < 0:
            if board[i][j] == board[i][j+1]:
                same += 1
            else:
                break
        else:
            if abs(board[i][j] - board[i][j + 1]) > 1:
                same = -1# 불가능
                break

            if abs(board[i][j] - board[i][j + 1]) == 1:
                if board[i][j] < board[i][j+1] and same >= 0:
                    if same >= L:
                        same = 1
                    else:
                        same = -1
                        break

                if board[i][j] > board[i][j + 1] and same >= 0:
                    same = -L + 1

            if board[i][j] == board[i][j + 1]:
                same += 1
    #한 행이 다 똑같거나 나머지 조건 만족하면 +1
    if same >= 0:
        ans += 1
#열

for i in range(N):
    same = 1
    for j in range(N-1):
        if same < 0:
            if board[j][i] == board[j + 1][i]:
                same += 1
            else:
                break
        else:
            if abs(board[j][i] - board[j + 1][i]) > 1:
                same = -1# 불가능
                break

            if abs(board[j][i] - board[j+1][i]) == 1:
                if board[j][i] < board[j+1][i] and same >= 0:
                    if same >= L:
                        same = 1
                    else:
                        same = -1
                        break

                if board[j][i] > board[j + 1][i] and same >= 0:
                    same = -L + 1

            if board[j][i] == board[j + 1][i]:
                same += 1

    #한 행이 다 똑같거나 나머지 조건 만족하면 +1
    if same >= 0:
        ans += 1

print(ans)


