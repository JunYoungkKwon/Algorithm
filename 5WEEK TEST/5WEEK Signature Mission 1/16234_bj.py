# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.

from collections import deque
N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]


def is_vaild(y, x):
    return 0 <= y < N and 0 <= x < N

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y_pos, x_pos, num_people, cnt_fed):
    visited = [[False] * N for _ in range(N)]
    deq = deque()
    deq.append((y_pos, x_pos, num_people, cnt_fed))
    visited[y_pos][x_pos] = True

    while deq:
        y, x, num, cnt =deq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_vaild(ny, nx) and not visited[ny][nx]:
                if L <= abs(country[y][x]- country[ny][nx]) <= R:
                    visited[ny][nx] = True
                    deq.append((ny, nx, num + country[ny][nx], cnt + 1))
    if cnt >= 2:
        return True

ans = 0
for i in range(N):
    for j in range(N):
        if bfs(i, j, country[i][j], 1):
            ans += 1
print(ans)