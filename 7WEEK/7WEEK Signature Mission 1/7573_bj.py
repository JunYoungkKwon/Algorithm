N, L, M = map(int, input().split())
fish = []
fish_net = []
ans = 0
r_ans = 0

for _ in range(M):
    a, b = map(lambda x:x-1, map(int, input().split()))
    fish.append((a, b))

def cnt_fish(ny, nx, y, x):
    cnt = 0
    for fi in fish:
        if ny > y:
            if nx > x:
                if y <= fi[0] <= ny and x <= fi[1] <= nx:
                    cnt += 1
            else:
                if y <= fi[0] <= ny and nx <= fi[1] <= x:
                    cnt += 1
        else:
            if nx > x:
                if ny <= fi[0] <= y and x <= fi[1] <= nx:
                    cnt += 1
            else:
                if ny <= fi[0] <= y and nx <= fi[1] <= x:
                    cnt += 1
    return cnt

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < N

def get_net():
    h = L // 2
    for i in range(1, h):
        fish_net.append((i, h-i))

def is_possible(k, fi):
    global ans
    for net in fish_net:
        # 좌상, 우상
        if k == 0:
            #피쉬가 네트의 가장 끝에 걸리게 하고 그 후 한칸씩 네트를 옮기며 체크
            fy = fi[0] - net[0]  # 현재 y좌표 + 네트 범위
            fx = fi[1] - net[1]  # 현재 x좌표 + 네트 범위
            lx = fi[1] + net[1]
            for i in range(fy, fi[0]):
                if is_valid(i, fx):
                    ans = max(ans, cnt_fish(i + net[0], fx, i, fi[1]))
            for j in range(fx, lx+1):
                    #범위 체크
                    if is_valid(fy, j):
                        # 범위 안 물고기 개수 체크
                        ans = max(ans, cnt_fish(fy, j + net[1], fi[0], j))
        # 좌하, 우하
        if k == 1:
            fy = fi[0] + net[0]
            fx = fi[1] - net[1]
            lx = fi[1] + net[1]
            for i in range(fy, fi[0], -1):
                if is_valid(i, fx):
                    ans = max(ans, cnt_fish(i + net[0], fx, i, fi[1]))
            for j in range(fx, lx):
                if is_valid(fy, j):
                    ans = max(ans, cnt_fish(fy, j + net[1], fi[0], j))
    return ans


#네트 종류 가져오기
get_net()
for fi in fish:
    for k in range(2):
        r_ans = max(r_ans, is_possible(k, fi))

print(r_ans)