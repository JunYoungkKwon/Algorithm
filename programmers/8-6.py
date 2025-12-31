import sys
sys.setrecursionlimit(10**6)

def solution(tickets):
    tickets.sort()
    n = len(tickets)
    visited = [False] * n
    path = ["ICN"]
    answer = []

    def dfs(now, cnt):
        if cnt == n:
            answer.append(path[:])
            return

        for i, (start, end) in enumerate(tickets):
            if not visited[i] and start == now:
                visited[i] = True
                path.append(end)
                dfs(end, cnt + 1)
                path.pop()
                visited[i] = False

    dfs("ICN", 0)
    return answer[0]
