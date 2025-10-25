N = int(input())
bomb = [list(input().strip()) for _ in range(N)]
visited = [list(input().strip()) for _ in range(N)]

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

result = [['.'] * N for _ in range(N)]
boom = False  # 지뢰를 밟았는지 체크

for y in range(N):
    for x in range(N):
        if visited[y][x] == 'x':  # 열린 칸
            if bomb[y][x] == '*':  # 지뢰를 밟았다면
                boom = True
            else:
                # 주변 지뢰 개수 세기
                cnt = 0
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and bomb[ny][nx] == '*':
                        cnt += 1
                result[y][x] = str(cnt)

# 지뢰를 밟은 경우 모든 지뢰 표시
if boom:
    for y in range(N):
        for x in range(N):
            if bomb[y][x] == '*':
                result[y][x] = '*'

# 출력
for row in result:
    print("".join(row))
