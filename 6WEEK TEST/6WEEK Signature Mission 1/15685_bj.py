# 첫째 줄에 드래곤 커브의 개수 N
# x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대
# 0,1,2,3
# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
#
# 0,0,0,3
#
# 0→(0)
# 1→(0)(↑(1))
# 2→↑(01)(←↑(21))
# 3→↑←↑(0121)(←↓←↑(2321))

dx = [1,0,-1,0]
dy = [0,-1,0,1]

N = int(input())
chk = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    chk[x][y] = 1


0
def dragon_curve(x, y, d_list, g):
    #조건 다시 한번 생각
    if g > 0:
        for d in d_list:
            x = dx[d] + x
            y = dy[d] + y
            chk[x][y] = 1
            d_list.append((d+1)//4)
        a_list.reverse()

        dragon_curve(x, y, d_list, g-1)








