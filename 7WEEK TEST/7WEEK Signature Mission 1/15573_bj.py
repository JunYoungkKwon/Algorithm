import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def can_mine(max_cost):
    visited = [[False]*M for _ in range(N)]
    q = deque()
    cnt = 0

    # 외곽에서 시작 가능한 칸들 중, cost ≤ max_cost 인 칸들을 큐에 넣기
    for j in range(M):
        if S[0][j] <= max_cost:
            visited[0][j] = True
            q.append((0,j))
            cnt += 1
        if N > 1 and S[N-1][j] <= max_cost:
            visited[N-1][j] = True
            q.append((N-1, j))
            cnt += 1
    for i in range(1, N-1):
        if S[i][0] <= max_cost:
            visited[i][0] = True
            q.append((i, 0))
            cnt += 1
        if M > 1 and S[i][M-1] <= max_cost:
            visited[i][M-1] = True
            q.append((i, M-1))
            cnt += 1

    # BFS / flood-fill
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and S[ni][nj] <= max_cost:
                visited[ni][nj] = True
                q.append((ni, nj))
                cnt += 1
                if cnt >= K:
                    return True
    return False

# 이분 탐색
left, right = 1, max(max(row) for row in S)
ans = right

while left <= right:
    mid = (left + right) // 2
    if can_mine(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
