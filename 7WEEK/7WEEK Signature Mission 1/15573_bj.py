from collections import deque
N, M, K = map(int, input().split())
mineral = [list(map(int, input().split())) for _ in range(N)]
lo = 0
hi = 1000**2 + 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# for i in range(N):
#     for j in range(M):
#         mineral[i][j] = 1


def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M

def is_possible(mid):
    chk = [[0] * M for _ in range(N)]
    q = deque()
    cnt = 0
    for i in range(N):
        if not i:
            for j in range(M):
                if mineral[i][j] <= mid:
                    chk[i][j] = 1
                    q.append((i, j))
                    cnt += 1

        else:
            if not chk[i][0] and mineral[i][0] <= mid:
                chk[i][0] = 1
                q.append((i, 0))
                cnt +=1
            if not chk[i][M-1] and mineral[i][M-1] <= mid:
                chk[i][M-1] = 1
                q.append((i, M-1))
                cnt +=1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid(ny, nx) and mineral[ny][nx] <= mid and not chk[ny][nx]:
                chk[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
    # for nn in range(N):
    #     print(*chk[nn])
    return cnt >= K

#강도를 이분 탐색으로 줄이기 거의 매개변수 같긴 함..
while lo + 1 < hi:
    mid = (lo + hi) // 2
    # print(f'lo = {lo} mid = {mid} hi = {hi}')
    if is_possible(mid):
        hi = mid
    else:
        lo = mid

print(hi)