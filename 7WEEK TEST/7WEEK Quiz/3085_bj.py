# 빨간색은C, 파란색은P, 초록색은Z, 노란색은Y
# 사탕의 색이 다른 인접한 두 칸을 고른다.
# 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
# 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
# 사탕의 최대 개수

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
ans = 0

def chk_candy():
    ans_candy = 0
    #일단 가로의 캔디만 측정
    for i in range(N):
        max_candy = 1
        for j in range(N):
            #같다면 캔디+1
            if j+1 < N and board[i][j] == board[i][j + 1]:
                max_candy += 1
            #다르다면 캔디 1로 초기화
            else:
                max_candy = 1
        ans_candy = max(ans_candy, max_candy)

    for j in range(N):
        max_candy = 1
        for i in range(N):
            #같다면 캔디+1
            if i+1 < N and board[i][j] == board[i+1][j]:
                max_candy += 1
            #다르다면 캔디 1로 초기화
            else:
                max_candy = 1
        ans_candy = max(ans_candy, max_candy)

    return ans_candy




for i in range(N):
    for j in range(N):
        #가로 바꾸기
        if j+1 < N and board[i][j] != board[i][j+1]:
            #사탕 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            #긴 부분 고르기
            ans = max(ans, chk_candy())
            #원래대로 사탕 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        #세로 바꾸기
        if i + 1 < N and board[i][j] != board[i+1][j]:
            # 사탕 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            # 긴 부분 고르기
            ans = max(ans, chk_candy())
            # 원래대로 사탕 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)


