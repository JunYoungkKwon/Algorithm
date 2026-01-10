# [벡준] 숨바꼭질
from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001
board = [0] * 100001

def bfs(start, t):
    deq = deque()
    deq.append((start, t))
    visited[start] = True

    while deq:
        pos,time = deq.popleft()
        if pos == K:
            return board[K]
        for i in [pos-1,pos+1,pos*2]:
            next_pos = i
            if 0<= next_pos <100001 and not visited[next_pos]:
                visited[next_pos] = True
                board[next_pos] = time+1
                deq.append((next_pos, time+1))

print(bfs(N, 0))
