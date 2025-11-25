import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())

# 그래프: 역 1~N, 튜브 N+1~N+M
graph = [[] for _ in range(N + M + 1)]

# 튜브 정보 입력
for tube_id in range(N + 1, N + M + 1):
    stations = list(map(int, input().split()))
    for s in stations:
        graph[s].append(tube_id)
        graph[tube_id].append(s)

# BFS
dist = [-1] * (N + M + 1)
dist[1] = 1  # 시작 역은 1개 방문한 것으로 카운트

q = deque([1])

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

# dist[N]이 정답인데, 중간에 튜브 노드도 거쳤으니 계산 조정 필요
# 실제로 역만 세면 (dist[N] + 1) / 2 형태지만,
# 시작을 1로 뒀기 때문에 역 노드에서만 방문한 횟수는 다음과 같다:

if dist[N] == -1:
    print(-1)
else:
    # 튜브 노드를 거치면 값이 1씩 증가되므로
    # 역만 카운트하려면 (dist[N] + 1) // 2
    print((dist[N] + 1) // 2)
