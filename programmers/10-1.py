from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    # 1️⃣ 그래프 구성
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 2️⃣ 거리 배열 (-1 = 미방문)
    dist = [-1] * (n + 1)
    dist[1] = 0

    q = deque([1])

    # 3️⃣ BFS
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    # 4️⃣ 가장 먼 거리 노드 개수
    max_dist = max(dist)
    return dist.count(max_dist)
