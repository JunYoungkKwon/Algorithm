from collections import deque

def bfs(start, target):
    visited = [False] * 10000
    parent = [-1] * 10000
    how = [''] * 10000

    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()
        if cur == target:
            break

        # D
        nxt = (cur * 2) % 10000
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            how[nxt] = 'D'
            q.append(nxt)

        # S
        nxt = 9999 if cur == 0 else cur - 1
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            how[nxt] = 'S'
            q.append(nxt)

        # L
        nxt = (cur % 1000) * 10 + cur // 1000
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            how[nxt] = 'L'
            q.append(nxt)

        # R
        nxt = (cur % 10) * 1000 + cur // 10
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            how[nxt] = 'R'
            q.append(nxt)

    # 🔁 경로 복원
    res = []
    cur = target
    while cur != start:
        res.append(how[cur])
        cur = parent[cur]

    return ''.join(reversed(res))

for _ in range(int(input())):
    A, target = map(int, input().split())
    print(bfs(A, target))
