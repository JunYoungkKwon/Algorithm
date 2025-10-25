A, B = input().split()

# 교차 글자 위치 찾기
for j, a in enumerate(A):
    if a in B:
        x = j            # A에서 위치
        y = B.index(a)   # B에서 첫 번째 등장 위치
        break

# 보드 초기화
board = [['.'] * len(A) for _ in range(len(B))]

# 세로로 B 넣기
for i in range(len(B)):
    board[i][x] = B[i]

# 가로로 A 넣기
for i in range(len(A)):
    board[y][i] = A[i]

# 출력
for row in board:
    print(''.join(row))
