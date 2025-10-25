from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001

def bfs():
    deq = deque()
    deq.append((N, 0))

    while deq:
        pos, time = deq.popleft()
        if pos == K:
            return time

        for i in (pos+1, pos-1, 2*pos):
            npos = i
            if 0<= npos <= 100000 and not visited[npos]:
                visited[npos] = True
                deq.append((npos, time+1))


print(bfs())