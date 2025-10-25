
#3차원만 배열만 만들면 다른 bfs 문제랑 다를 게 없는 문제
#chk = True 안해주면 메모리 초과 나니깐 한번 더 확인
from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

d= 0

def is_valid_coord(z, y, x):
    return 0 <= z < L and 0 <= y < R and 0 <= x < C

def bfs(z, y, x, d):
    q = deque()
    q.append((z, y, x, d))
    while q:
        z, y, x, d = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if is_valid_coord(nz, ny, nx) and not chk[nz][ny][nx]:
                if adj[nz][ny][nx] == 'E':
                    chk[nz][ny][nx] = True
                    print(f'Escaped in {d+1} minute(s).')
                    return
                if adj[nz][ny][nx] == '.':
                    chk[nz][ny][nx] = True
                    q.append((nz, ny, nx, d+1))
    print("Trapped!")

while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    adj = []
    for _ in range(L):
        adj.append([input().strip() for _ in range(R)])
        input()
    chk = [[[False] * C for _ in range(R)] for _ in range(L)]

    for z in range(L):
        for y in range(R):
            for x in range(C):
                if adj[z][y][x] == 'S' and is_valid_coord(z, y, x) and not chk[z][y][x]:
                    chk[z][y][x] = True
                    bfs(z, y, x, d)