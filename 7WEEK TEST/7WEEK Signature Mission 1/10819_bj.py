N = int(input())
arr = list(map(int, input().split()))

visited = [False] * N
picked = []
ans = 0
def bfs(depth, total):
    global ans

    if depth == N:
        ans = max(ans, total)
        return ans

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            if depth == 0:
                picked.append(arr[i])
                bfs(depth+1, total)
                picked.pop()
            else:
                picked.append(arr[i])
                bfs(depth+1, total + abs(picked[-2]-picked[-1]))
                picked.pop()
            visited[i] = False


bfs(0,0)
print(ans)