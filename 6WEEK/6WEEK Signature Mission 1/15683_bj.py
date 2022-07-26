#혼자 하다가 헤메서 결국 참고함
import copy

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M

def watch(y, x, direction, board):
    for d in direction:
        ny, nx = y, x
        # 특정 방향으로 벽을 만나거나 사무실을 벗어나기 전까지 탐색
        while True:
            ny += direction_list[d][0]
            nx += direction_list[d][1]
            # 맵 내 위치
            if is_valid(ny, nx):
                # 벽을 만난 경우
                if board[ny][nx] == 6:
                    break
                # 새로운 감시가능 영역일 경우
                elif board[ny][nx] == 0:
                    board[ny][nx] = '#'
            # 맵 외 위치
            else:
                break

def cnt_zero(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    return cnt

def dfs(board, depth):
    global answer
    # 종료 조건: 모든 CCTV 탐색
    if depth == len(cctv):
        # 사각지대 최솟값
        answer = min(answer, cnt_zero(board))
        return
    else:
        # 사무실 정보 깊은 복사
        graph_copy = copy.deepcopy(board)
        y, x, cctv_type = cctv[depth]
        for cctv_dir in cctv_direction[cctv_type]:
            # CCTV 감시영역 구하는 함수 호출
            watch(y, x, cctv_dir, graph_copy)
            # 현재 Case에서 타 모든 CCTV 재귀적 탐색
            dfs(graph_copy, depth + 1)
            # CCTV를 다른 방향으로 회전시킨 후 재탐색하기 위함
            graph_copy = copy.deepcopy(board)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv = []
answer = int(1e9)
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv.append((i, j, board[i][j]))
direction_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# CCTV별 이동 가능한 방향
cctv_direction = [
    [],
    [[0], [1], [2], [3]],  # 1번 CCTV
    [[0, 1], [2, 3]],  # 2번 CCTV
    [[0, 2], [0, 3], [1, 2], [1, 3]],  # 3번 CCTV
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],  # 4번 CCTV
    [[0, 1, 2, 3]]  # 5번 CCTV
]

dfs(board, 0)
print(answer)
