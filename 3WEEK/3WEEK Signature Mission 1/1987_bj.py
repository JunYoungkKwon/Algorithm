#list에 알파벳을 넣고 in list 를 통해 조회하니깐 시간 초과
# list에 알파벳을 넣지 않고 문자열에 알파벳을 더하는 것으로 도전
# input 함수 바꿔줘서 간신히 시간 내에 해결
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [input() for _ in range(N)]
chk = [[False] * M for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def dfs(y, x, str_chk):
    global ans
    ans = max(ans, len(str_chk))
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and not chk[ny][nx]:
            if board[ny][nx] not in str_chk:
                chk[ny][nx] = True
                dfs(ny, nx, str_chk + board[ny][nx])
                chk[ny][nx] = False

ans = 1
chk[0][0] = True
dfs(0, 0, board[0][0])
print(ans)
