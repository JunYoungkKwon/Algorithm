from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houses.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


ans = 200 * N
for combi in combinations(chickens, M):
    tot = 0  # 도시의 치킨 거리
    for house in houses:
        tot += min(dist(house, chicken) for chicken in combi)

    ans = min(ans, tot)

print(ans)
