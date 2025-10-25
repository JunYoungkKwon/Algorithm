from collections import deque

N, K = map(int, input().split())
def bfs():
    visited = [0] * 100001
    deq = deque()
    deq.append(N)
    while deq:
        x = deq.popleft()
        if x == K:
            return visited[x]
        for nx in (x - 1, x + 1, 2 * x):  # 세 가지 이동
            if 0 <= nx <= 100000 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                deq.append(nx)

print(bfs())