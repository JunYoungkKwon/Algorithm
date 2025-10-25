# 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 1초 후에 X-1 또는 X+1로 이동 1초 후에 2*X
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후
from collections import deque
N, K = map(int, input().split())
visited = [False] * 100001

def bfs():
    #여기서 튜플 형태로 넣어야하는지 아니면 그냥 넣어도 되는지 해결해야함
    deq = deque()
    deq.append((N, 0))
    visited[N] = True

    while deq:
        pos, second = deq.popleft()

        #수빈이가 동생을 찾았다면
        if pos == K:
            return second

        for npos in ( pos+1, pos-1, pos*2 ):
            #간 곳 체크 해야되는지 아닌지 해결해야함
            if  0 <= npos <= 100000 and not visited[npos]:
                visited[npos] = True
                deq.append((npos, second+1))

print(bfs())