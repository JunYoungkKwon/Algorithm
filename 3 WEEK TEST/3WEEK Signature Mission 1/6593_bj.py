# 상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)
# 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하) 이동
# 대각선으로 이동하는 것은 불가능
# L, R, C로 시작한다.
# L(1 ≤ L ≤ 30)은 상범 빌딩의 층 수이다.
# R(1 ≤ R ≤ 30)과 C(1 ≤ C ≤ 30)는 상범 빌딩의 한 층의 행과 열의 개수
# 입력의 끝은 L, R, C가 모두 0으로 표현된다.
# 지나갈 수 없는 칸은 '#'
# 비어있는 칸은 '.'
#
# Escaped in x minute(s).
# Trapped!
from collections import deque
import sys
input = sys.stdin.readline

dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []
    q = deque()

    for l in range(L):
        floor = [list(input().rstrip()) for _ in range(R)]
        building.append(floor)
        input()  # 층 사이의 빈 줄
        for i in range(R):
            for j in range(C):
                if floor[i][j] == 'S':
                    q.append((l, i, j, 0))

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    escaped = False

    while q:
        z, y, x, t = q.popleft()
        if building[z][y][x] == 'E':
            print(f"Escaped in {t} minute(s).")
            escaped = True
            break

        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C:
                if not visited[nz][ny][nx] and building[nz][ny][nx] != '#':
                    visited[nz][ny][nx] = True
                    q.append((nz, ny, nx, t + 1))

    if not escaped:
        print("Trapped!")

