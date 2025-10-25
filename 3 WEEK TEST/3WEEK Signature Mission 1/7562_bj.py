import sys
from collections import deque

input = sys.stdin.readline

# l(4 ≤ l ≤ 300)

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def is_valid(y,x):
    return 0 <= y < l and 0 <= x < l

def bfs():

    while deq:
        ay, ax, ans = deq.popleft()
        if ay == fy and ax == fx:
            return ans
        for i in range(8):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if is_valid(ny, nx) and not visited[ny][nx]:
                visited[ny][nx] = 1
                deq.append((ny, nx, ans+1))


for _ in range(int(input())):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    y, x = map(int, input().split())
    fy, fx = map(int, input().split())
    if y == fy and x == fx:
        print(0)
    else:
        deq = deque()
        deq.append((y, x, 0))
        visited[y][x] = 1
        print(bfs())


