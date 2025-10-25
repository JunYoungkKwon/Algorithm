# from collections import deque
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
#
# visit = [False for _ in range(N+1)]
#
# graph = [[] for _ in range(N+1)]
#
# count = 0
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
#
# def bfs(start):
#     deq = deque([start])
#
#     while deq:
#         y = deq.popleft()
#         for x in graph[y]:
#             if not visit[x]:
#                 visit[x] = True
#                 deq.append(x)
#
#
# for i in range(1, N+1):
#     if not visit[i]:
#         count += 1
#         visit[i] = True
#         bfs(i)
# print(count)

import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘리기
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 간선 정보
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
