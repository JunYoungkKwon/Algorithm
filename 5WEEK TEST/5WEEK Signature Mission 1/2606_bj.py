N = int(input())
M = int(input())

# 인접 리스트 생성
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

dfs(1)
# 1번 제외하고 감염된 컴퓨터 수 계산
print(sum(visited) - 1)
