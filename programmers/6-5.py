import heapq

def solution(n, costs):
    # 인접 리스트
    graph = [[] for _ in range(n)]
    for a, b, cost in costs:
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    visited = [False] * n
    pq = [(0, 0)]  # (비용, 시작 정점)
    answer = 0
    count = 0

    while pq and count < n:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        answer += cost
        count += 1

        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_cost, next_node))

    return answer
